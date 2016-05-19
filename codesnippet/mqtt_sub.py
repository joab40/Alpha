import paho.mqtt.client as mqtt
import time
import json
import os
import sys


topic = "alphahead"

basepath = os.path.dirname(os.path.abspath(__file__))
ymlfile = basepath + "/../etc/alpha_config.yml"
libpath = basepath + "/../test/"

if libpath not in sys.path:
        sys.path.insert(1, libpath)

import camera_rotor_class

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
  client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  #print msg.topic + " " + str(msg.payload)
  decode = json.loads(msg.payload)
  print "subscribed info:",int(decode['xcord']),":end"
  testa = test.focus(int(decode['xcord']))
  if testa != None:
    procent_mov = 100 - testa
    print "testobjectprint:",(procent_mov),":end"
    os.system('sudo echo 0=' + str(procent_mov) + '% > /dev/servoblaster')


  #time.sleep(3)

test = camera_rotor_class.camera_rotor(0,640,20,180,5)
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("iot.eclipse.org", 1883, 60)
client.connect("localhost", 1883, 60)

client.loop_forever()
