from attr import dataclass
from influxdb_client import WriteOptions


@dataclass
class InfluxDbSettings:
    organization: str
    token: str
    url: str

    write_options: WriteOptions
