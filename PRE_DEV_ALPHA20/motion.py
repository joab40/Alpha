#!/usr/bin/python
import time
import paho.mqtt.client as mqtt
import json
import os
from daemon import runner



class Motion():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/motion.pid'
        self.pidfile_timeout = 5

    def run(self):
        #while True:
        print("Starting motion")
        os.system('/usr/bin/motion -n')

app = Motion()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()