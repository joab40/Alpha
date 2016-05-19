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


client2 = mqtt.Client()
#client2.connect("iot.eclipse.org", 1883, 60)
client2.connect(yconfig['mqtt']['host'], yconfig['mqtt']['port'], 60)
print "Connected to ", yconfig['mqtt']['host'], " Port: ", yconfig['mqtt']['port']
topic = yconfig['mqtt']['topic']['stt']
print "Publishing to topic: ", topic

while True:
  area = 1
  indata = raw_input('-> ')
  if indata == 'exit' or indata == 'quit':
      sys.exit(0)
  message = json.dumps({yconfig['stt']['mqttparam']: indata, 'id': area, 'time': time.time()})
  client2.publish(topic,message)
  print "sent!"