import time
import signal
from iot_processor.broker import Broker

class Application:

    def __init__(self, options):
        signal.signal( signal.SIGINT, lambda signal, frame: self._signal_handler() )
        self.terminated = False
        self.broker = Broker(hostname = options.mqtt_host, port = options.mqtt_port)

    def _signal_handler(self):
        self.terminated = True

    def MainLoop(self):
        self.broker.start()

        while not self.terminated:
            time.sleep(1)

        self.broker.stop()
