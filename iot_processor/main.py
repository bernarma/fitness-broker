import argparse
import queue
import sys
import signal
import time

from iot_processor.broker import Broker

# https://stackoverflow.com/questions/5055042/whats-the-best-practice-using-a-settings-file-in-python

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()

    # TODO: externalise into a configuration file from args
    broker = Broker(hostname = "localhost", port = 1883)
    broker.start()

    signal.signal(signal.SIGINT, signal_handler)

    print('Press Ctrl+C')
    try:
        while True:
            signal.pause()
    except AttributeError:
        # signal.pause() is missing for Windows; wait 1ms and loop instead
        while True:
            time.sleep(1)
