#!/usr/bin/python
import time
import paho.mqtt.client as mqtt
import json
from daemon import runner

topic = "alpha/cam"

def on_connect(client, userdata, rc):
        client.subscribe(topic)

def on_message(client, userdata, msg):
        decode = json.loads(msg.payload)
        print "subscribed info:",int(decode['xcord']),":end"
        #client.disconnect()

class Servo():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/servo.pid'
        self.pidfile_timeout = 5
        self.topic = "alpha/cam"



    def run(self):
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("localhost", 1883, 60)
        client.loop_forever()

app = Servo()
daemon_runner = runner.DaemonRunner(app)
daemon_runner.do_action()