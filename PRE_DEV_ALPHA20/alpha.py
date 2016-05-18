#!/usr/bin/env python
# -*- coding: utf-8 -*-
import aiml
import os
import speech_recognition as sr
import pyvona
import argparse
import yaml
import time
import logging
import paho.mqtt.client as mqtt
import json
from commands import *
import sys


reload(sys)
sys.setdefaultencoding('utf8')

basepath = os.path.dirname(os.path.abspath(__file__))
ymlfile = basepath + "/../etc/alpha_config.yml"
libpath = basepath + "/../lib/"

if libpath not in sys.path:
        sys.path.insert(1, libpath)
import led_class

import modules_class

# Topic wildcard
topic = "alpha/#"

def readyaml(yfile):
    logger.info("readyaml             - read yaml file            [\033[0;32mREAD\033[0m] on admin on host: %s ", yfile)
    # Add check for file exist/read
    with open(yfile, 'r') as f:
        config =  yaml.load(f)
    f.close()
    return config

def on_connect(client, userdata, rc):
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print msg.topic + " " + str(msg.payload)
    # X cord from camera eye
    if msg.topic == yconfig['mqtt']['topic']['cam']:
        print "recv cam topic"
        client.publish('test','blargh')






#if __name__ == '__main__':
if "a" == "a":
        Version = "2.00"
        parser = argparse.ArgumentParser(description='sasha')
        parser.add_argument("--textonly", "-t", help="Text only, disable all voice", action="store_true")
        parser.add_argument("--ttsonly", "-s", help="Text only, disable all voice", action="store_true")
        parser.add_argument('-d', '--loglevel',default='', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL' ], help='Default WARNING')
        parser.add_argument('-f', '--logfile', default='', help='Path to Logfile')
        args = parser.parse_args()
        if args.logfile:
            numeric_level = getattr(logging, args.loglevel.upper(), None)
            FORMAT = '%(asctime)-15s %(levelname)s    - %(name)s - %(message)s'
            logging.basicConfig(format=FORMAT,level=numeric_level,filename=args.logfile)
            logger = logging.getLogger('Islay Of Mist')
        else:
            numeric_level = getattr(logging, args.loglevel.upper(), None)
            FORMAT = '%(asctime)-15s %(levelname)s    - %(name)s - %(message)s'
            logging.basicConfig(format=FORMAT,level=numeric_level)
            logger = logging.getLogger('Islay Of Mist')
        logger.debug("__main__: Starting ervers: %s ",Version)

        try:
            # Read Configurations yaml config file
            yconfig = readyaml(ymlfile)
        except:
            print "Couldnt find ymlfile !?", ymlfile
            sys.exit(1)


        moduler=modules_class.modules('../etc/alpha_config.yml')
        moduler.show()
        moduler.start()



        exit(0)
        topic = yconfig['mqtt']['topic']['alpha']
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("localhost", 1883, 60)
        client.loop_forever()