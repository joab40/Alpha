#!/usr/bin/env python
# -*- coding: utf-8 -*-
import aiml
import os
import pyvona
import argparse
import yaml
import time
import logging
import paho.mqtt.client as mqtt
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

basepath = os.path.dirname(os.path.abspath(__file__))
ymlfile = basepath + "/../etc/alpha_config.yml"
libpath = basepath + "/../lib/"



if libpath not in sys.path:
        sys.path.insert(1, libpath)
import readYaml as getconfig
yconfig = getconfig.readyaml(ymlfile)

from messager_mqtt import create_message,extract_message,create_from_message,bounche_message

client2 = mqtt.Client()
#client2.connect("iot.eclipse.org", 1883, 60)
#client2.connect(yconfig['mqtt']['host'], yconfig['mqtt']['port'], 60)
print "Connected to ", yconfig['mqtt']['host'], " Port: ", yconfig['mqtt']['port']
topic = yconfig['mqtt']['topic']['stt']
print "Publishing to topic: ", topic

while True:
  area = 1
  indata = raw_input('-> ')

  #message = json.dumps({yconfig['stt']['mqttparam']: indata,'sender': 'stt', 'id': '0', 'area': '0', 'bounce': '0', 'time': time.time()})
  message = create_message(indata,'stt')
  print "print topic: ", extract_message(message,text='show')
  print "test bounce: ", bounche_message(message)
  print "create from message: ", create_from_message(message,'changing module text','tts')
  client2.connect(yconfig['mqtt']['host'], yconfig['mqtt']['port'], 60)
  client2.publish(topic,message)
  client2.disconnect()
  print "sending this: ", message
  if indata == 'avsluta' or indata == 'exit':
      sys.exit(0)