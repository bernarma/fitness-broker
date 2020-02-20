import sys
import signal
import time
import iot_processor
import paho.mqtt.client as mqtt

from threading import Thread

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_disconnect(client, userdata,rc=0):
    print("Disconnected result code "+str(rc))
    client.loop_stop()

def connect_to_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect

    client.connect("mqtt.eclipse.org", 1883, 60)
    client.loop_start()

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
connect_to_mqtt()

print('Press Ctrl+C')
try:
    while True:
        signal.pause()
except AttributeError:
    # signal.pause() is missing for Windows; wait 1ms and loop instead
    while True:
        time.sleep(1)
