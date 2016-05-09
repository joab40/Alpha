#!/usr/bin/env python
# -*- coding: utf-8 -*-

########## IN PROGRESS #####################

import sys
import time
import os
import yaml
import logging


reload(sys)
sys.setdefaultencoding('utf8')

class modules(object):
    def __init__(self,ymlfile):
        # creating object
        self.yfile = ymlfile
        self.yconfig
        self.modules={}
        self.modules_daemon_starts={}
        self.modules_daemon_stopps={}
        self.modules_daemon_status={}
        self.modules_daemon_restarts={}

    def readyaml(self,yfile):
        logger.info("readyaml             - read yaml file            [\033[0;32mREAD\033[0m] on admin on host: %s ", yfile)
        # Add check for file exist/read
        with open(yfile, 'r') as f:
            config =  yaml.load(f)
        f.close()
        return config

    def start(self,modules='all'):
        print "starts: ",modules

    def stop(self,modules='all'):
        print "stopping: ", modules

    def restart(self,modules='all'):
        print "restarts: ", modules
    def status(self,modules='all'):
        print "status modules: ", modules

    def show(self):
        print self.modules_daemon_status
        print self.modules_daemon_restarts
        print self.modules_daemon_starts
        print self.modules_daemon_stopps


    def predefine_status(self):
        if yconfig['mqtt']['enable']:
            print "Mqtt mosquitto       [enable]"
        if yconfig['motion']['enable']:
            print "Motion daemon        [enable]"
        if yconfig['camera']['enable']:
            print "Subscribe to camera  [enable]"
        if yconfig['wolframalpha']['enable']:
            print "Wolframalpha         [enable]"
        if yconfig['bot']['alice']:
            print "Alice bot            [enable]"
        if yconfig['gpio']['raspberrypi']:
            print "Led GPIO             [enable]"
        if yconfig['translate']['enable']:
            print "Transalte to swedish [enable]"
        if yconfig['pyvonna']['enable']:
            print "Pyvonna TTS          [enable]"
        if yconfig['keylemon']['enable']:
            print "Keylemon reqognition [enable]"







#test = alphamqtt('localhost','1883','alphahead')
#test.pub('333')
#time.sleep(1)
#test.off()
# test.off()
# test.blink_on('red',"1")
