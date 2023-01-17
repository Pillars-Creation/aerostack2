""" Launch the AS2 platform behaviors. """
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    """ Launch the AS2 platform behaviors. """
    return LaunchDescription([
        DeclareLaunchArgument('namespace'),
        DeclareLaunchArgument('use_sim_time', default_value='false'),

        DeclareLaunchArgument('follow_path_plugin_name'),
        DeclareLaunchArgument('follow_path_speed', default_value="0.5"),
        DeclareLaunchArgument('follow_path_threshold', default_value="0.3"),
        Node(
            package='as2_movement_behaviors',
            executable='follow_path_behavior_node',
            namespace=LaunchConfiguration('namespace'),
            parameters=[
                {"namespace": LaunchConfiguration('namespace')},
                {"use_sim_time": LaunchConfiguration('use_sim_time')},
                {"plugin_name": LaunchConfiguration(
                    'follow_path_plugin_name')},
                {"follow_path_speed": LaunchConfiguration(
                    'follow_path_speed')},
                {"follow_path_threshold": LaunchConfiguration(
                    'follow_path_threshold')}
            ],
            output='screen',
            emulate_tty=True
        ),

        DeclareLaunchArgument('goto_plugin_name'),
        DeclareLaunchArgument('goto_speed', default_value="0.5"),
        DeclareLaunchArgument('goto_threshold', default_value="0.3"),
        Node(
            package='as2_movement_behaviors',
            executable='goto_behavior_node',
            namespace=LaunchConfiguration('namespace'),
            parameters=[
                {"namespace": LaunchConfiguration('namespace')},
                {"use_sim_time": LaunchConfiguration('use_sim_time')},
                {"plugin_name": LaunchConfiguration('goto_plugin_name')},
                {"goto_speed": LaunchConfiguration(
                    'goto_speed')},
                {"goto_threshold": LaunchConfiguration('goto_threshold')}
            ],
            output='screen',
            emulate_tty=True
        ),

        DeclareLaunchArgument('land_plugin_name'),
        DeclareLaunchArgument('land_speed', default_value="0.2"),
        Node(
            package='as2_movement_behaviors',
            executable='land_behavior_node',
            namespace=LaunchConfiguration('namespace'),
            parameters=[
                {"namespace": LaunchConfiguration('namespace')},
                {"use_sim_time": LaunchConfiguration('use_sim_time')},
                {"plugin_name": LaunchConfiguration('land_plugin_name')},
                {"land_speed": LaunchConfiguration(
                    'land_speed')}
            ],
            output='screen',
            emulate_tty=True
        ),

        DeclareLaunchArgument('takeoff_plugin_name'),
        DeclareLaunchArgument('takeoff_height', default_value="1.0"),
        DeclareLaunchArgument('takeoff_speed', default_value="0.2"),
        DeclareLaunchArgument('takeoff_threshold', default_value="0.1"),
        Node(
            package='as2_movement_behaviors',
            executable='takeoff_behavior_node',
            namespace=LaunchConfiguration('namespace'),
            parameters=[
                {"namespace": LaunchConfiguration('namespace')},
                {"use_sim_time": LaunchConfiguration('use_sim_time')},
                {"plugin_name": LaunchConfiguration('takeoff_plugin_name')},
                {"takeoff_height": LaunchConfiguration(
                    'takeoff_height')},
                {"takeoff_speed": LaunchConfiguration(
                    'takeoff_speed')},
                {"takeoff_threshold": LaunchConfiguration('takeoff_threshold')}
            ],
            output='screen',
            emulate_tty=True
        ),
    ])
