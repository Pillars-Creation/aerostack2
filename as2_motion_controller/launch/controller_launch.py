# Copyright 2024 Universidad Politécnica de Madrid
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""Launch file for the controller manager node."""

__authors__ = 'Pedro Arias Pérez, Rafael Pérez Seguí'
__copyright__ = 'Copyright (c) 2024 Universidad Politécnica de Madrid'
__license__ = 'BSD-3-Clause'

import os

from ament_index_python.packages import get_package_share_directory
from as2_core.declare_launch_arguments_from_config_file import DeclareLaunchArgumentsFromConfigFile
from as2_core.launch_configuration_from_config_file import LaunchConfigurationFromConfigFile
from as2_core.launch_plugin_utils import get_available_plugins
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import EnvironmentVariable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


def get_package_config_file():
    """Return the package config file."""
    package_folder = get_package_share_directory('as2_motion_controller')
    return os.path.join(package_folder,
                        'config/motion_controller_default.yaml')


def generate_launch_description():
    """Return the launch description."""
    package_folder = get_package_share_directory('as2_motion_controller')
    plugin_config_file = PathJoinSubstitution([
        package_folder,
        'plugins', LaunchConfiguration('plugin_name'), 'config/controller_default.yaml'
    ])
    plugin_available_modes_config_file = PathJoinSubstitution([
        package_folder,
        'plugins', LaunchConfiguration('plugin_name'), 'config/available_modes.yaml'
    ])
    launch_description = LaunchDescription([
        DeclareLaunchArgument('log_level',
                              description='Logging level',
                              default_value='info'),
        DeclareLaunchArgument('use_sim_time',
                              description='Use simulation clock if true',
                              default_value='false'),
        DeclareLaunchArgument('namespace',
                              description='Drone namespace',
                              default_value=EnvironmentVariable(
                                  'AEROSTACK2_SIMULATION_DRONE_ID')),
        DeclareLaunchArgument('plugin_name',
                              description='Plugin name',
                              choices=get_available_plugins(
                                  'as2_motion_controller')),
        DeclareLaunchArgumentsFromConfigFile(
            name='motion_controller_config_file',
            source_file=get_package_config_file(),
            description='Configuration file'),
        DeclareLaunchArgument(
            'plugin_available_modes_config_file',
            description='Plugin available modes configuration file',
            default_value=plugin_available_modes_config_file),
        DeclareLaunchArgumentsFromConfigFile(
            name='plugin_config_file',
            source_file=plugin_config_file,
            description='Plugin configuration file'),
        Node(
            package='as2_motion_controller',
            executable='as2_motion_controller_node',
            name='controller_manager',
            namespace=LaunchConfiguration('namespace'),
            output='screen',
            arguments=['--ros-args', '--log-level',
                       LaunchConfiguration('log_level')],
            emulate_tty=True,
            parameters=[
                {
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                    'plugin_name': LaunchConfiguration('plugin_name'),
                    'plugin_available_modes_config_file': LaunchConfiguration(
                        'plugin_available_modes_config_file')
                },
                LaunchConfigurationFromConfigFile(
                    'motion_controller_config_file',
                    default_file=get_package_config_file()),
                LaunchConfigurationFromConfigFile(
                    'plugin_config_file',
                    default_file=plugin_config_file),
            ]
        )])
    return launch_description
