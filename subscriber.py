"""This script is an example of subscriber to CloudMQTT Broker"""

from urllib.parse import urlparse
import os
import paho.mqtt.client as mqtt
import time

# Define event callbacks
def on_message(mosq, obj, msg):
    # message = str(msg.payload)
    print('Topic: {}/{}'.format(msg.topic, msg.payload.decode('utf-8')))

def on_subscribe(mosq, obj, mid, granted_qos):
    print('Subscribed: {}, QoS: {}'.format(str(mid), str(granted_qos)))


client = paho.client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect('mqtt.eclipse.org')
client.subscribe('myhome/+/kitchen')

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = client.loop()
    time.sleep(2)
#print('Reconnect: ' + str(rc))