#TODO: when message received add to the command list (process in order but acknowledge priority - what are the priority classifications)
# Need to define the use cases of received messages - can only think of one at the moment: Customer Command

#TODO: outbound queue - will need multiple depending on the type of message - unless we use one single queue for all messages with a priority

import sys
import signal
import time
import iot_processor
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import queue
from threading import Thread

def worker(q):
    while True:
        item = q.get()
        
        # TODO: process item and send to target MQTT topic: do_work(item)
        print(f"Processing Item: {item}")

        client.publish("paho/test/single", "boo")

        # TODO: need to handle a failure to publish if the broker is down for whatever reason
        
        q.task_done()

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    queue.put(msg.payload)

    # TODO: handle message - this is basically a command that we need to do something with
    # TODO: send response for message by adding to another queue - a listener on that queue will take the message and send to the client

def on_publish(client,userdata,result):
    print("data published \n")

def on_disconnect(client, userdata,rc=0):
    print("Disconnected result code "+str(rc))
    if rc != 0:
        print ("Unexpected disconnection. Reconnecting...")
        connect_to_mqtt()
    else :
        print ("Disconnected successfully")
        client.loop_stop()

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    
    # need to have an indicator to STOP listening for commands
    client.unsubscribe("$SYS/#")

    # exit when all messages have been sent
    # TODO: only process specific category messages (not iot messages) - also send back a generic disconnect/shutdown message
    print(queue.qsize())
    queue.join()

    client.disconnect()

    sys.exit(0)

# client to listen for messages
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
client.on_publish = on_publish

queue = queue.Queue()
t = Thread(target=worker, args=(queue,))
t.daemon = True
t.start()

signal.signal(signal.SIGINT, signal_handler)

def connect_to_mqtt():
    client.connect(HOST, PORT, 60)
    client.loop_start()

#HOST = "mqtt.eclipse.org"
HOST = "localhost"
PORT = 1883
connect_to_mqtt()

print('Press Ctrl+C')
try:
    while True:
        signal.pause()
except AttributeError:
    # signal.pause() is missing for Windows; wait 1ms and loop instead
    while True:
        time.sleep(1)
