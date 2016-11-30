#!/usr/bin/env python
# -*- coding: utf-8 -*-

########## IN PROGRESS #####################

import sys
import time
import os
import yaml
import logging
import paho.mqtt.client as mqtt
import json
import argparse

from messager_mqtt import create_message,extract_message,create_from_message,bounche_message

logger = logging.getLogger(__name__)

reload(sys)
sys.setdefaultencoding('utf8')

class modules(object):
    def __init__(self,ymlfile):
        # creating object
        self.yfile=ymlfile
        self.yconfig={}
        self.modules={}
        self.modules_daemon_starts={}
        self.modules_daemon_stopps={}
        self.modules_daemon_status={}
        self.modules_daemon_restarts={}
        self.sendmqtt_status={}
        self.sendmqtt_stopps = {}
        self.readyaml(self.yfile)
        # Init modules config
        self.moduleconfig()


    def readyaml(self,yfile):

        logger.debug("readyaml             - read yaml file            [\033[0;32mREAD\033[0m] on admin on host: %s ", yfile)
        # Add check for file exist/read
        with open(yfile, 'r') as f:
            self.yconfig =  yaml.load(f)
        f.close()

    def moduleconfig(self):
        for ytest in self.yconfig:
            try:
                chk_enable = self.yconfig[ytest]['enable']
                logger.debug("moduleconfig - exist and enable is: [\033[0;33m%s\033[0m] -> %s ", self.yconfig[ytest]['enable'], ytest )
                if self.yconfig[ytest]['enable']:
                    self.modules[ytest]=self.yconfig[ytest]['enable']
            except KeyError, e:
                logger.warning("moduleconfig - module not correct defined [\033[0;31m%s\033[0m]", ytest)

        for modulekey in self.modules.keys():
            if self.modules[modulekey]:
                try:
                    if self.yconfig[modulekey]['daemon']:
                        self.modules_daemon_starts[modulekey]=self.yconfig[modulekey]['starts']
                except KeyError, e:
                    self.logger.warning("module start parameter is missing: %s", modulekey)
                try:
                    if self.yconfig[modulekey]['daemon']:
                        self.modules_daemon_stopps[modulekey]=self.yconfig[modulekey]['stopps']
                except KeyError, e:
                    logger.warning("module stopps parameter is missing: %s", modulekey)
                try:
                    if self.yconfig[modulekey]['daemon']:
                        self.modules_daemon_restarts[modulekey]=self.yconfig[modulekey]['restarts']
                except KeyError, e:
                    logger.warning("module restarts parameter is missing: %s", modulekey)
                try:
                    if self.yconfig[modulekey]['daemon']:
                        self.modules_daemon_status[modulekey]=self.yconfig[modulekey]['status']
                except KeyError, e:
                    logger.warning("module status parameter is missing: %s", modulekey)



    def start(self,modul='all'):
        if modul == 'all':
            for modulekey in self.modules_daemon_starts.keys():
                logger.debug("start - os.system execute modul [\033[0;32m%s\033[0m]: ",self.modules_daemon_starts[modulekey] )
                os.system(self.modules_daemon_starts[modulekey])
        else:
            try:
                os.system(self.modules_daemon_starts[modul])
            except KeyError, e:
                logger.warning('start - module doesnt exist %s: ', modul)

        #print "starts: ",modules
        #print self.modules_daemon_starts

    def stop(self,modules='all'):
        logger.debug('stop - Nothing is executing [\033[0;33m%s\033[0m]: ', modules)
        #print self.modules_daemon_stopps

    def restart(self,modules='all'):
        logger.debug('restart - Nothing is executing [\033[0;33m%s\033[0m]: ', modules)

    def status(self,modules='all'):
        logger.debug('status - Nothing is executing [\033[0;31m%s\033[0m]: ',modules )
        #print "status modules: ", self.modules_daemon_status


    def show(self):
        logger.debug('show - Defined scripts in %s', self.yfile)
        print "-----------------------------------------------------------------------------------------------------"
        for module in self.modules_daemon_starts.keys():
            print "Startscript   : ",self.modules_daemon_starts[module]
        print "-----------------------------------------------------------------------------------------------------"
        for module in self.modules_daemon_stopps.keys():
            print "Stopscript    : ",self.modules_daemon_stopps[module]
        print "-----------------------------------------------------------------------------------------------------"
        for module in self.modules_daemon_restarts.keys():
            print "Restartscript : ",self.modules_daemon_restarts[module]
        print "-----------------------------------------------------------------------------------------------------"
        for module in self.modules_daemon_status.keys():
            print "Statusscript  : ",self.modules_daemon_status[module]
        print "-----------------------------------------------------------------------------------------------------"
       
        #        print self.modules_daemon_status
#        print self.modules_daemon_restarts
#        print self.modules_daemon_starts
#        print self.modules_daemon_stopps


    def predefine_status(self):
        if self.yconfig['mqtt']['enable']:
            print "Mqtt mosquitto       [enable]"
        if self.yconfig['motion']['enable']:
            print "Motion daemon        [enable]"
        if self.yconfig['camera']['enable']:
            print "Subscribe to camera  [enable]"
        if self.yconfig['wolframalpha']['enable']:
            print "Wolframalpha         [enable]"
        if self.yconfig['bot']['alice']:
            print "Alice bot            [enable]"
        if self.yconfig['gpio']['raspberrypi']:
            print "Led GPIO             [enable]"
        if self.yconfig['translate']['enable']:
            print "Transalte to swedish [enable]"
        if self.yconfig['pyvonna']['enable']:
            print "Pyvonna TTS          [enable]"
        if self.yconfig['keylemon']['enable']:
            print "Keylemon reqognition [enable]"

    def verify_modules(self):

        # we asume that system modules always have status defined i alpha_config.yaml
        logger.debug('  verify_modules - send verification')
        for modulekey in self.modules.keys():
            try:
                logger.debug('  verify_modules - sending [\033[0;32m%s\033[0m]', self.modules_daemon_status[modulekey])
                self.sendmqtt_status[modulekey] = self.modules_daemon_status[modulekey]
            except KeyError,e:
                logger.warning('verify_modules - module not defined correct [\033[0;31m%s\033[0m]',modulekey)

        for sendmodule in self.sendmqtt_status.keys():
            vclient = mqtt.Client()
            vclient.connect(self.yconfig['mqtt']['host'], self.yconfig['mqtt']['port'], 60)
            logger.debug('  verify_modules - Sending verify module [\033[0;32m%s\033[0m] topic: %s', self.sendmqtt_status[sendmodule],self.yconfig[sendmodule]['mqtttopic'])
            # This one is right from alpha, therefore bounced should be 1. STT is bypassed
            message = json.dumps({self.yconfig[sendmodule]['mqttparam']: self.sendmqtt_status[sendmodule],'sender': 'moduleclass', 'id': 0, 'area': '0','bounce': '1', 'time': time.time()})
            #message = create_message(self.sendmqtt_status[sendmodule],'verify_module')
            vclient.publish(self.yconfig[sendmodule]['mqtttopic'], message)
            vclient.disconnect()

    def send_stop(self):
        #vclient = mqtt.Client()
        #vclient.connect(self.yconfig['mqtt']['host'], self.yconfig['mqtt']['port'], 60)
        # we asume that system modules always have status defined i alpha_config.yaml
        #print "This should send a [module][stopps] mqtt to modules"
        for modulekey in self.modules.keys():
            try:
                logger.debug('  send_stop - Sending mqtt stop [\033[0;32m%s\033[0m]',self.modules_daemon_stopps[modulekey])
                self.sendmqtt_stopps[modulekey] = self.modules_daemon_stopps[modulekey]
            except KeyError, e:
                logger.warning('send_stop - Modul status not correct defined [\033[0;31m%s\033[0m]',modulekey)
        # print "almost done: ", self.sendmqtt_status


        for sendmodule in self.sendmqtt_stopps.keys():
            vclient = mqtt.Client()
            #print "SENDING MQTT publish: ", self.sendmqtt_stopps[sendmodule]
            vclient.connect(self.yconfig['mqtt']['host'], self.yconfig['mqtt']['port'], 60)
            logger.debug('  send_stop - Sending mqtt stop [\033[0;31m%s\033[0m] topic: %s',sendmodule,self.yconfig[sendmodule]['mqtttopic'])
            message = json.dumps(
                {self.yconfig[sendmodule]['mqttparam']: self.sendmqtt_stopps[sendmodule],'sender': 'moduleclass', 'id': 0,'area': '0','bounce': '0', 'time': time.time()})
            vclient.publish(self.yconfig[sendmodule]['mqtttopic'], message)
            vclient.disconnect()

if __name__ == '__main__':
    Version = "1.00"
    parser = argparse.ArgumentParser(description='modules_class')
    parser.add_argument('-c', '--control', default='verify',
                        choices=['verify', 'show', 'predefined', 'start', 'send_stop','stop'], help='Default WARNING')
    parser.add_argument('-d', '--loglevel', default='INFO',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='Default WARNING')
    parser.add_argument('-f', '--logfile', default='', help='Path to Logfile')
    args = parser.parse_args()
    if args.logfile:
        numeric_level = getattr(logging, args.loglevel.upper(), None)
        FORMAT = '%(asctime)-15s %(levelname)s    - %(name)s - %(message)s'
        logging.basicConfig(format=FORMAT, level=numeric_level, filename=args.logfile)
        logger = logging.getLogger('modules_class')
    else:
        numeric_level = getattr(logging, args.loglevel.upper(), None)
        FORMAT = '%(asctime)-15s %(levelname)s    - %(name)s - %(message)s'
        logging.basicConfig(format=FORMAT, level=numeric_level)
        logger = logging.getLogger('modules_class')
    logger.debug("__main__: Starting ervers: %s ", Version)

#    LOGLEVEL = 'DEBUG'
    test = modules('../etc/alpha_config.yml')
    if args.control == 'verify':
        test.verify_modules()
    elif args.control == 'show':
        test.show()
    elif args.control == 'start':
        test.start()
    elif args.control == 'send_stop':
        test.send_stop()
    elif args.control == 'stop':
        test.stop()
    elif args.control == 'predefined':
        test.predefine_status()


