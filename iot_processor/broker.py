from threading import Thread

import paho.mqtt.client as mqtt
import queue

class Broker:

    @property
    def client(self):
            return self._client

    @property
    def hostname(self):
            return self._hostname

    @property
    def port(self):
            return self._port

    def __init__(self, hostname, port):
        self._hostname = hostname
        self._port = port
        self._queue = queue.Queue()
        self._client = mqtt.Client()

    def __connect_mqtt_broker(self):
        self.client.connect(self.hostname, self.port, 60)
        self._client.loop_start()

    def __disable_command_receiver(self):
        self._client.unsubscribe("$SYS/#")

    def __worker(self):
        while True:
            item = self._queue.get()
            print(f"Processing Item: {item}")

            # TODO: process item and send to target MQTT topic: do_work(item)
            self.client.publish("paho/test/single", item)
            # TODO: need to handle a failure to publish if the broker is down for whatever reason
            
            self._queue.task_done()
            
    def __on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        self.client.subscribe("$SYS/#") # TODO: externalise into configuration
    
    def __on_message(self, client, userdata, msg):
        print(f"{msg.topic} {msg.payload}")
    
    def __on_disconnect(self, client, userdata, rc=0):
        print(f"Disconnected with result code {rc}")
        if rc != 0:
            print ("Unexpected disconnection. Reconnecting...")
            self.__connect_mqtt_broker()
        else :
            print ("Disconnected successfully")
            self.client.loop_stop()
    
    def __on_publish(self, client, userdata, result):
        print(f"Data published with result code {result}")

    def start(self):
        # spawn worker thread to process command queue
        t = Thread(target=self.__worker)
        t.daemon = True
        t.start()

        self.client.on_connect = self.__on_connect
        self.client.on_message = self.__on_message
        self.client.on_disconnect = self.__on_disconnect
        self.client.on_publish = self.__on_publish

        # connect to mqtt - this creates another thread to receive commands from mqtt
        self.__connect_mqtt_broker()
