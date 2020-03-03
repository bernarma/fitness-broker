from threading import Thread
from iot_processor.repeated_timer import RepeatedTimer

import paho.mqtt.client as mqtt
import queue
import time
import iot_processor.messages.example_pb2 as pb2

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

    @property
    def num_workers(self):
            return self._num_workers

    def __init__(self, hostname, port, num_workers):
        self._hostname = hostname
        self._port = port
        self._queue = queue.Queue(maxsize=0)
        self._client = mqtt.Client()
        self._connected = False
        self._num_workers = num_workers

    def __connect_mqtt_broker(self):
        self.client.connect(self.hostname, self.port, 60)
        self._client.loop_start()

    def __disable_command_receiver(self):
        self._heartbeat.stop()

    def __worker(self):
        while True:
            item = self._queue.get()

            try:
                print(f"Processing Item: {item}")

                sample = pb2.Person()
                sample.id = 1234
                to_client = sample.SerializeToString()
                print(to_client)
                
                self.client.publish("param/param/param/test", to_client)
                
            except: # log error for malformed message
                pass
            
            self._queue.task_done()
            
    def __on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        
        if rc==0:
            self._connected = True
            self._heartbeat = RepeatedTimer(1, self._send_heartbeat)
    
    def __on_message(self, client, userdata, msg):
        print(f"{msg.topic} {msg.payload}")
        self._queue.put(msg.payload)
    
    def __on_disconnect(self, client, userdata, rc=0):
        print(f"Disconnected with result code {rc}")
        if rc != 0:
            print ("Unexpected disconnection. Reconnecting...")
            self.__connect_mqtt_broker()
        else :
            print ("Disconnected successfully")
            self._client.loop_stop()
            self._connected = False
    
    def __on_publish(self, client, userdata, result):
        print(f"Data published with result code {result}")

    def _send_heartbeat(self):
        heartbeat = pb2.Heartbeat()
        self.client.publish("server/heartbeat", heartbeat.SerializeToString())

    def stop(self):
        self.__disable_command_receiver()
        self._queue.join()
        self._client.disconnect()
        
        while self._connected: # wait until disconnected
            time.sleep(.1)

    def start(self):
        # spawn worker threads to process command queue
        for _ in range(self._num_workers):
            worker = Thread(target=self.__worker)
            worker.daemon = True
            worker.start()
  
        self.client.on_connect = self.__on_connect
        self.client.on_message = self.__on_message
        self.client.on_disconnect = self.__on_disconnect
        self.client.on_publish = self.__on_publish

        # connect to mqtt - this creates another thread to receive commands from mqtt
        self.__connect_mqtt_broker()
