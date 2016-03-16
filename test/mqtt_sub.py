import paho.mqtt.client as mqtt
import time

topic = "alphahead"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
  client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  print msg.topic + " " + str(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("iot.eclipse.org", 1883, 60)
client.connect("localhost", 1883, 60)

client.loop_forever()
