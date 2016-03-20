#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os
import paho.mqtt.client as mqtt
import json


reload(sys)
sys.setdefaultencoding('utf8')

class alphamqtt(object):
    def __init__(self,broker,brokerport, topic):
        # creating object
        self.topic = topic
        self.broker = broker
        self.brokerport = brokerport
        self.count = 0
        self.client2 = mqtt.Client()
        self.client2.connect(broker, brokerport, 60)

    def pub(self,amsg):
        self.count +=1
        message = json.dumps({'xcord': amsg, 'id': self.count, 'time': time.time()})
        print message
        self.client2.publish(self.topic, message)

    def sub(self):
        print "subscribe"






#test = alphamqtt('localhost','1883','alphahead')
#test.pub('333')
#time.sleep(1)
#test.off()
# test.off()
# test.blink_on('red',"1")
