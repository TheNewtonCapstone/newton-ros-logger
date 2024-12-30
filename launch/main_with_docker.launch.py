import os.path

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    share_path = get_package_share_directory('newton_ros_logger')
    docker_compose_path = os.path.join(share_path, '..', "docker/newton-influxdb.compose.yaml")

    influxdb_docker_process = ExecuteProcess(
        cmd=['docker', 'compose', '-f', docker_compose_path, 'up', '--no-recreate', '--remove-orphans'],
        output='screen',
    )

    newton_ros_logger_node = Node(
        package='newton_ros_logger',
        executable='main',
        name='newton_ros_logger',
    )

    return LaunchDescription([
        influxdb_docker_process,
        newton_ros_logger_node,
    ])
