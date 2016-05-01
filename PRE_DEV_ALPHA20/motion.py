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
import subprocess
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



def readyaml(yfile):
    logger.info("readyaml             - read yaml file            [\033[0;32mREAD\033[0m] on admin on host: %s ", yfile)
    # Add check for file exist/read
    with open(yfile, 'r') as f:
        config =  yaml.load(f)
    f.close()
    return config

def start():
    print "starting motion daemon"

def stop():
    print "stopping motion daemon"
    os.system('')

if __name__ == '__main__':
        Version = "0.01"
        parser = argparse.ArgumentParser(description='sasha')
        parser.add_argument("--start", "-s", help="start motion as deamon", action="store_true")
        parser.add_argument("--stop", "-k", help="stop motion", action="store_true")
        parser.add_argument("--restart", "-r", help="stop motion", action="store_true")
        parser.add_argument('-d', '--loglevel',default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL' ], help='Default WARNING')
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

        logger.info("main                 - yaml read                 [\033[0;32mOK\033[0m] %s " ,yconfig['motion']['enable'])

        if yconfig['motion']['path']:
            motionpath = yconfig['motion']['path']
        else:
            motionpath = False
            logger.critical("Did not find a path in yaml file for motion")
            exit(1)

        if yconfig['motion']['config']:
            configfile = yconfig['motion']['config']
        else:
            configfile = False
            logger.critical("Did not find config file for motion in yaml file")

        if yconfig['motion']['pidfil']:
            pidfile = yconfig['motion']['pidfil']
        else:
            pidfile = False
            logger.critical("PID file info is missing in yaml config file")

        if args.start:
            logger.info("Starting Motion")
            os.system("sudo " + yconfig['motion']['path'] + " -c " + yconfig['motion']['config'] )
        if args.stop:
            logger.info("Stopping Motion")
            mpid = subprocess.check_output('cat ' + yconfig['motion']['pidfil'], shell = True)
            os.system('sudo kill -9 ' + str(mpid) )

        if args.restart:
            logger.info("Restarting motion")
            mpid = subprocess.check_output('cat ' + yconfig['motion']['pidfil'], shell = True)
            os.system('sudo kill -9 ' + str(mpid) )
            time.sleep(2)
            os.system("sudo " + yconfig['motion']['path'] + " -c " + yconfig['motion']['config'] )



