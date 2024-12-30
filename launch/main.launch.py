from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    newton_ros_logger_node = Node(
        package='newton_ros_logger',
        executable='main',
        name='newton_ros_logger',
    )

    return LaunchDescription([
        newton_ros_logger_node,
    ])
