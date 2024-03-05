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

"""Launch file for point gimbal behavior node."""

from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, EnvironmentVariable


def generate_launch_description():
    """Launch point gimbal behavior node."""
    return LaunchDescription([
        DeclareLaunchArgument('namespace', description='Drone namespace',
                              default_value=EnvironmentVariable('AEROSTACK2_SIMULATION_DRONE_ID')),
        DeclareLaunchArgument('use_sim_time', default_value='false'),
        DeclareLaunchArgument('log_level', default_value='info'),
        DeclareLaunchArgument('gimbal_name', description='Name of the gimbal'),
        DeclareLaunchArgument('gimbal_frame_id', description='Gimbal frame id'),
        DeclareLaunchArgument('gimbal_base_frame_id', description='Gimbal base frame id'),
        DeclareLaunchArgument('gimbal_orientation_threshold',
                              description='Gimbal orientation threshold'),
        DeclareLaunchArgument('tf_timeout_threshold', description='TF timeout threshold'),
        Node(
            package='as2_behaviors_perception',
            executable='point_gimbal_behavior_node',
            namespace=LaunchConfiguration('namespace'),
            output='screen',
            arguments=['--ros-args', '--log-level',
                       LaunchConfiguration('log_level')],
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'gimbal_name': LaunchConfiguration('gimbal_name'),
                'gimbal_frame_id': LaunchConfiguration('gimbal_frame_id'),
                'gimbal_base_frame_id': LaunchConfiguration('gimbal_base_frame_id'),
                'gimbal_orientation_threshold':
                    LaunchConfiguration('gimbal_orientation_threshold'),
                'tf_timeout_threshold': LaunchConfiguration('tf_timeout_threshold'),
            }],
            emulate_tty=True,
        ),
    ])
