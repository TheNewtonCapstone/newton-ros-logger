# Newton ROS Logger

This package assembles all topics from the Newton project and logs them to a InfluxDB database. Although the package is designed to work with the Newton project, it can be used with any other project that uses ROS.

## Requirements
- ROS Humble (installed system-wide or through Conda with Robostack)
- InfluxDB Python client (installed through pip)
- Docker (optional, for running InfluxDB locally; disregard if you have a remote InfluxDB instance)