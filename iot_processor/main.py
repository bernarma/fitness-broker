import queue
import logging
import sys
import signal
import time
import configargparse

from iot_processor.broker import Broker

if __name__ == '__main__':
    p = configargparse.ArgParser(default_config_files=['/etc/app/conf.d/*.conf', '~/iot.config'])
    p.add('-c', '--config', required=True, is_config_file=True, help='config file path')
    p.add('--mqtt_host', default='localhost', help='MQTT server hostname')
    p.add('--mqtt_port', type=int, default=1883, help='MQTT server port number')
    options = p.parse_args()

    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
    broker = Broker(hostname = options.mqtt_host, port = options.mqtt_port)

    def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        broker.stop()
        sys.exit(0)

    broker.start()
    signal.signal(signal.SIGINT, signal_handler)
    #logging.info('Press Ctrl+C')
    print('Press Ctrl+C')

    try:
        while True:
            signal.pause()
    except AttributeError:
        # signal.pause() is missing for Windows; wait 1ms and loop instead
        while True:
            time.sleep(1)
