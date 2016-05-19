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

print yconfig['mqtt']['topic']['stt']
exit(0)

client2 = mqtt.Client()
#client2.connect("iot.eclipse.org", 1883, 60)
client2.connect("pi", 1883, 60)
count = 0

topic = "alpha/stt"

while True:
  count +=1
  nb = raw_input('-> ')
  if nb == 'exit' or nb == 'quit':
      sys.exit(0)
  message = json.dumps({'temp': '30', 'id': count, 'time': time.time()})
  client2.publish(topic, nb)
  print "sent!",count