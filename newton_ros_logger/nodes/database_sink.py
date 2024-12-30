from typing import Optional

from influxdb_client import InfluxDBClient, QueryApi, WriteApi
from rclpy.node import Node, MsgType

from ..db import InfluxDbSettings
from ..types import TypeMap, SubscriptionMap


class DatabaseSinkNode(Node):
    def __init__(self, connection_settings: InfluxDbSettings, topics_to_track: TypeMap):
        super().__init__("newton_ros_logger")

        self._connection_settings: InfluxDbSettings = connection_settings
        self._topics_to_track: TypeMap = topics_to_track

        self._db_client: Optional[InfluxDBClient]
        self._db_write_client: Optional[WriteApi]
        self._db_query_client: Optional[QueryApi]

        self._tracked_subs: SubscriptionMap = {}

        self._create_db()
        self._create_subs()

    def __del__(self):
        self._db_client.close()

    def _create_db(self) -> None:
        self._db_client = InfluxDBClient(
            url=self._connection_settings.url,
            token=self._connection_settings.token,
            org=self._connection_settings.organization,
        )
        self._db_write_client = self._db_client.write_api(
            write_options=self._connection_settings.write_options,
        )
        self._db_query_client = self._db_client.query_api()

    def _create_subs(self) -> None:
        for topic_name, topic_type in self._topics_to_track.items():
            self._tracked_subs[topic_name] = self.create_subscription(
                msg_type=topic_type,
                topic=topic_name,
                callback=self._write_to_db,
                qos_profile=10,
            )

    def _write_to_db(self, msg: MsgType) -> None:
        print(msg)
