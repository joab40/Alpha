#!/usr/bin/python
import time
import paho.mqtt.client as mqtt
import json
from daemon import runner



class Cam():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/cam.pid'
        self.pidfile_timeout = 5

    def run(self):
        self.client = mqtt.Client()
        self.client.connect("localhost", 1883, 60)
        count = 0
        topic = "alpha/cam"
        while True:
            print("Starting read focus from cam")
            count +=1
            message = json.dumps({'xcord': '30', 'id': count, 'time': time.time()})
            self.client.publish(topic, message)
            print "sent!",count
            time.sleep(3)

app = Cam()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()
