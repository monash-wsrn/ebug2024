import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # This node is the central controller (i.e., Boids Algorithm)
    Boids = Node(
        package = 'ebug_principal',
        executable = 'BoidsService',
        name = 'BoidsService',
    )

    StaticTransformAprilTag0 = Node(
        package = 'tf2_ros',
        executable = 'static_transform_publisher',
        arguments = ['--x', '0.11', '--y', '0.0', '--z', '0', '--yaw', '1.5708', '--pitch', '0.0', '--roll', '1.5708', '--frame-id', 'map', '--child-frame-id', 'apriltag_0']
    )

    StaticTransformAprilTag1 = Node(
        package = 'tf2_ros',
        executable = 'static_transform_publisher',
        arguments = ['--x', '0.0', '--y', '0.15', '--z', '0', '--yaw', '3.1416', '--pitch', '0', '--roll', '1.5708', '--frame-id', 'map', '--child-frame-id', 'apriltag_1']
    )

    StaticTransformAprilTag2 = Node(
        package = 'tf2_ros',
        executable = 'static_transform_publisher',
        arguments = ['--x', '-0.11', '--y', '0.0', '--z', '0', '--yaw', '-1.5708', '--pitch', '0', '--roll', '1.5708', '--frame-id', 'map', '--child-frame-id', 'apriltag_2']
    )


    StaticTransformAprilTag3 = Node(
        package = 'tf2_ros',
        executable = 'static_transform_publisher',
        arguments = ['--x', '0.0', '--y', '-0.15', '--z', '0', '--yaw', '0', '--pitch', '0', '--roll', '1.5708', '--frame-id', 'map', '--child-frame-id', 'apriltag_3']
    )


    return LaunchDescription([
        DeclareLaunchArgument(
            'use_ebug_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        StaticTransformAprilTag0,
        StaticTransformAprilTag1,
        StaticTransformAprilTag2,
        StaticTransformAprilTag3,
        Boids
    ])