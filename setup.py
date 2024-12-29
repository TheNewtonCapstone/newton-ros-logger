import os
from glob import glob

from setuptools import setup

package_name = 'newton_ros_logger'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools', 'influxdb-client'],
    zip_safe=True,
    maintainer='TheNewtonCapstone',
    maintainer_email='the.newton.capstone@gmail.com',
    description='A ROS2 logger for the Newton project',
    license='GPL-3.0-only',
    entry_points={
        'console_scripts': [
            'main = newton_ros_logger.main:main'
        ],
    },
)
