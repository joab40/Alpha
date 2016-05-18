#!/usr/bin/env python
# -*- coding: utf-8 -*-

########## IN PROGRESS #####################

import sys
import time
import os
import yaml
import logging

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
        self.readyaml(self.yfile)
        self.moduleconfig()


    def readyaml(self,yfile):

        #logger.info("readyaml             - read yaml file            [\033[0;32mREAD\033[0m] on admin on host: %s ", yfile)
        # Add check for file exist/read
        with open(yfile, 'r') as f:
            self.yconfig =  yaml.load(f)
        f.close()
        #return config

    def moduleconfig(self):
        for ytest in self.yconfig:
            #print "ytest ", ytest
            try:
                chk_enable = self.yconfig[ytest]['enable']
                #logger.debug("module exist and enable is: [%s] -> %s ", yconfig[ytest]['enable'], ytest )
                if self.yconfig[ytest]['enable']:
                    self.modules[ytest]=self.yconfig[ytest]['enable']
            except KeyError, e:
                #logger.debug("Pass module not correct defined: %s ", ytest)
                print("pass module not correct defined")

        for modulekey in self.modules.keys():
            if self.modules[modulekey]:
                #print "TRUE"
                try:
                    if self.yconfig[modulekey]['daemon']:
                        self.modules_daemon_starts[modulekey]=self.yconfig[modulekey]['starts']
                except KeyError, e:
                    self.logger.warning("module start parameter is missing: %s", modulekey)
                    #print "error 1"
                try:
                    if self.yconfig[modulekey]['daemon']:
                        self.modules_daemon_stopps[modulekey]=self.yconfig[modulekey]['stopps']
                except KeyError, e:
                    logger.warning("module stopps parameter is missing: %s", modulekey)
                    #print "error 2"
                try:
                    if self.yconfig[modulekey]['daemon']:
                        self.modules_daemon_restarts[modulekey]=self.yconfig[modulekey]['restarts']
                except KeyError, e:
                    logger.warning("module restarts parameter is missing: %s", modulekey)
                    #print "error 3"
                try:
                    if self.yconfig[modulekey]['daemon']:
                        self.modules_daemon_status[modulekey]=self.yconfig[modulekey]['status']
                except KeyError, e:
                    logger.info("module status parameter is missing: %s", modulekey)
                    #print "error 4"
            #else:
            #    print "FALSE"
            #print ": ", modulekey, " value: ", self.modules[modulekey]

    def start(self,modules='all'):
        print "starts: ",modules
        print self.modules_daemon_starts

    def stop(self,modules='all'):
        print "stopping: ", modules
        print self.modules_daemon_stopps

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







#test = modules('../etc/alpha_config.yml')
#test.start()
#test.stop()
#test.predefine_status()
#test.show()
#time.sleep(1)
#test.off()
# test.off()
# test.blink_on('red',"1")
