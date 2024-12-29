# example.launch.py

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # start a newton_ros_logger_node in the turtlesim1 namespace
    newton_ros_logger_node = Node(
        package='newton_ros_logger',
        namespace='sim',
        executable='main',
        name='newton_ros_logger',
    )

    return LaunchDescription([
        newton_ros_logger_node,
    ])
