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
from messager_mqtt import create_message,extract_message,create_from_message,bounche_message

# Topic wildcard
topic = "alpha/#"

def readyaml(yfile):
    """
    Read config file
    :param yfile:
    :return:
    """
    logger.info("readyaml             - read yaml file            [\033[0;32mREAD\033[0m] on admin on host: %s ", yfile)
    # Add check for file exist/read
    with open(yfile, 'r') as f:
        config =  yaml.load(f)
    f.close()
    return config

def on_connect(client, userdata, rc):
    """
    Alpha Subscribes on a Topic /alpha/*
    :param client:
    :param userdata:
    :param rc:
    :return:
    """
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    """
    Incomming message on topic /alpha/*
    :param client:
    :param userdata:
    :param msg:
    :return:
    """
    #print msg.topic + " " + str(msg.payload)
    logger.debug('on_message - Incomming to %s msg: [\033[0;32m%s\033[0m]',msg.topic,str(msg.payload) )

    # This code will find and greate a releation data
    # For the sending module.
    # Next is to determ where this module whant to send its data

    ### THIS Should ba changed to extract SENDER instead of topic
    ### Message module = extract_message(message,sender='show')

    #incomming_message_from_modul = msg.topic.split('/')
    #on_message_module = incomming_message_from_modul[1]
    on_message_module = extract_message(msg.payload,sender='get')
    logger.debug('on_message - SPLIT get module Name \033[0;31m%s\033[0m]', on_message_module)
    # Try to get module relation
    temporary_relation_list = []
    try:
        for moduele_relation in yconfig[on_message_module]['relation'].split():
            temporary_relation_list.append(moduele_relation)

    except KeyError,e:
        logger.warning('on_message - Module \033[0;32m%s\033[0m] have missing relation configuration', on_message_module)

    try:
        decode = json.loads(msg.payload)
        bounce_number = decode['bounce']
        logger.debug('on_message - Bounced number of times \033[0;32m%s\033[0m]', bounce_number)
    except KeyError,e:
        logger.debug('on_message - Module and bounce number missing from message \033[0;31m%s\033[0m]',on_message_module)
    except ValueError, e:
        logger.warning('on_message - Missing Value \033[0;31mbounce\033[0m] in message')
        logger.warning('on_message - Failed message \033[0;31m%s\033[0m]',str(msg.payload))
    # Next step is to send module message regarding relation to next module
    try:
        sending_to_next_modul = temporary_relation_list[int(bounce_number)]
        logger.debug(
            'on_message - It seems like this module message whants to go to \033[0;32m%s\033[0m] bounced nr of times %s',
            sending_to_next_modul, bounce_number)
    except IndexError, e:
        logger.debug('on_message - well this whent out of index \033[0;31mFAILED\033[0m]')
        sending_to_next_modul = False

    if  sending_to_next_modul:
        ''' If registred info status. Add this info ALIVE to memory Here'''
        if yconfig[temporary_relation_list[int(bounce_number)]]['enable']:
            logger.debug('on_message - Module \033[0;32m%s\033[0m] is \033[0;32mENABLE\033[0m] sending..',temporary_relation_list[int(bounce_number)])
            bounced_msg = bounche_message(msg.payload)
            ''' In future, add logging to DB here'''
            ''' ------- Sending to a Module -----'''
            ''' Would be nice to verify modules existens here'''
            client.publish(yconfig[temporary_relation_list[int(bounce_number)]]['mqtttopic'], bounced_msg)
        elif yconfig[temporary_relation_list[int(bounce_number)]]['enable'] == False:
            logger.debug('on_message - Module \033[0;31m%s\033[0m] is \033[0;31mOFFLINE\033[0m] resend to alpha',temporary_relation_list[int(bounce_number)])
            bounced_msg = bounche_message(msg.payload)
            client.publish(msg.topic, bounced_msg)

        else:
            logger.debug('on_message - Message destination is \033[0;31mNOTOK\033[0m] ', msg.payload)
            # Eventual this messege should go to TTS. Some one need to know that this failed.
    else:
        logger.debug('on_message - Message is lost \033[0;31mNOTOK\033[0m]')

    # Verify messages in dict - memory - if there is no more relations to try. Then this is message is completed.
    # Remember this message. json should have a status field

    # HARDCODED Recived data from system module chatbot
    #if msg.topic == yconfig['mqtt']['topic']['chatbot'] and yconfig['chatbot']['enable']:
    #    print "^- Message from CHATBOT"

    ''' Temporary fix for shutdown '''
    ''' -------------------------- '''
    if msg.topic == yconfig['mqtt']['topic']['stt'] and yconfig['stt']['enable']:
         decode = json.loads(msg.payload)
         message = decode[yconfig['stt']['mqttparam']]
         if message == yconfig['main']['quit']:
             client.disconnect()
             moduler.send_stop()
             exit(0)



#if __name__ == '__main__':
if "a" == "a":
        Version = "2.00"
        parser = argparse.ArgumentParser(description='sasha')
        parser.add_argument("--textonly", "-t", help="Text only, disable all voice", action="store_true")
        parser.add_argument("--ttsonly", "-s", help="Text only, disable all voice", action="store_true")
        parser.add_argument('-d', '--loglevel',default='WARNING', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL' ], help='Default WARNING')
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
            logger = logging.getLogger('Alpha')
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
        # This is a mqtt call to modules. please verify your existens
        # And reply to Alpha
        time.sleep(5)
        moduler.verify_modules()

        topic = yconfig['mqtt']['topic']['alpha']
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("localhost", 1883, 60)
        client.loop_forever()