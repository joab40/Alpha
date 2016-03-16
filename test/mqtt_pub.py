import paho.mqtt.client as mqtt
import time
import json

client2 = mqtt.Client()
#client2.connect("iot.eclipse.org", 1883, 60)
client2.connect("localhost", 1883, 60)

topic = "alphahead"

message = json.dumps({'temp': '30', 'id': '1', 'time': time.time()})
while True:
  client2.publish(topic, message)
  print "sent!"
  time.sleep(2)
