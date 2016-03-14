#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import RPi.GPIO as GPIO
except ImportError:
    pass
    #print 'You need RPi.GPIO in %s ', libpath
    #sys.exit(1)

import sys
import time
import os
import yaml

basepath = os.path.dirname(os.path.abspath(__file__))
ymlfile = basepath + "/../etc/alpha_config.yml"
libpath = basepath + "/../lib/"

reload(sys)
sys.setdefaultencoding('utf8')


def readyaml(yfile):
    with open(yfile, 'r') as f:
        config = yaml.load(f)
    f.close()
    return config


class led(object):
    def __init__(self):
        # creating object
        self.ycolor = readyaml(ymlfile)
        self.color = 'None'

    def enable(self):
        if self.ycolor['gpio']['raspberrypi']:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(self.color, GPIO.OUT)

    def disable(self):
        print "cleanup"

    def on(self, color_value):
        if self.ycolor['gpio']['raspberrypi']:
            self.color = self.ycolor['gpio'][color_value]
            self.enable()
            GPIO.output(self.color, GPIO.HIGH)

    def off(self):
        if self.ycolor['gpio']['raspberrypi']:
            GPIO.output(self.color, GPIO.LOW)

    def blink_on(self, color_value, intervall):
        if self.ycolor['gpio']['raspberrypi']:
            print "blink"
            self.enable()
            self.on(color_value)
            time.sleep(1)
            self.off()

    def blink_off(self):
        print "blink off"

    def blink(self, color, time):
        print "just blink"


#test = led()
#test.on('green')
#time.sleep(1)
#test.off()
# test.off()
# test.blink_on('red',"1")
