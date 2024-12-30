import rclpy
from influxdb_client.client.write_api import SYNCHRONOUS
from newton_ros.msg import ImuMsg, ContactsMsg
from newton_sim_ros.msg import SimulationImuMsg, SimulationContactsMsg

from .db import InfluxDbSettings
from .nodes import DatabaseSinkNode


def main():
    rclpy.init()

    connection_settings = InfluxDbSettings(
        organization="newton",
        token="T84_NroliJCt8BeotYnhryx4mK5YQKlebNolOcfY3SxNlzlKx1vFLp6zl4W-aRtK23MdYEs91GTY3We9CD3l2w==",
        url="http://localhost:8086",
        write_options=SYNCHRONOUS,
    )
    sink = DatabaseSinkNode(connection_settings, {
        "/sim/imu": SimulationImuMsg,
        "/imu": ImuMsg,
        "/sim/contact": SimulationContactsMsg,
        "/contact": ContactsMsg,
    })

    rclpy.spin(sink)

    sink.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
