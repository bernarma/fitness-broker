import queue
import logging
import sys
import signal
import time
import configargparse
from iot_processor.application import Application

if __name__ == '__main__':
    p = configargparse.ArgParser(default_config_files=['/etc/app/conf.d/*.conf', '~/iot.config'])
    p.add('-c', '--config', required=True, is_config_file=True, help='config file path')
    p.add('--mqtt_host', default='localhost', help='MQTT server hostname')
    p.add('--mqtt_port', type=int, default=1883, help='MQTT server port number')
    p.add('--workers', type=int, default=1, help='Number of workers to process the command queue')
    options = p.parse_args()

    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')

    app = Application(options)
    app.MainLoop()