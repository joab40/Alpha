#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os
import sys

basepath = os.path.dirname(os.path.abspath(__file__))
ymlfile = basepath + "/../etc/alpha_config.yml"
libpath = basepath + "/../lib/"

if libpath not in sys.path:
        sys.path.insert(1, libpath)

try:
        import mqtt_class
except ImportError:
        print 'You need mqtt_class in %s ',libpath
        sys.exit(1)


sender = mqtt_class.alphamqtt('localhost','1883','alphahead')
filename = '/tmp/motion.log'
f = subprocess.Popen(['tail','-F',filename],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
while True:
    line = f.stdout.readline()
    if 'jpg' in line:
        #line.split()
        line = line.replace('jpg','')
        line = line.replace('.','')
        line = line.replace('-',' ')
        line = line.rsplit(None, 1)[-1]
        sender.pub(line)
        print line
