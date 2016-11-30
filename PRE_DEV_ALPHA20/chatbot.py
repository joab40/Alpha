#!/usr/bin/python
import time
import paho.mqtt.client as mqtt
import json
from daemon import runner
import yaml
import os,sys
import logging
from lockfile import LockTimeout
import aiml

basepath = os.path.dirname(os.path.abspath(__file__))
ymlfile = basepath + "/../etc/alpha_config.yml"
libpath = basepath + "/../lib/"
LOGLEVEL = 'DEBUG'


if libpath not in sys.path:
        sys.path.insert(1, libpath)

from messager_mqtt import create_message,extract_message,create_from_message,bounche_message

#topic = "alpha/chatbotproc"

def readyaml(yfile):
    #logger.info("readyaml             - read yaml file            [\033[0;32mREAD\033[0m] on admin on host: %s ", yfile)
    # Add check for file exist/read
    with open(yfile, 'r') as f:
        config =  yaml.load(f)
    f.close()
    return config

def on_connect(client, userdata, rc):
        client.subscribe(listen_topic)

def on_message(client, userdata, msg):
        #logger.debug('  on_message - msg.topic    [\033[0;32m%s\033[0m]', msg.topic)
        #logger.debug('  on_message - msg.payload  [\033[0;32m%s\033[0m]', str(msg.payload))
        #print msg.topic + " " + str(msg.payload)
        decode = json.loads(msg.payload)
        logger.debug('  on_message - from [\033[0;32m%s\033[0m] decode json  [\033[0;32m%s\033[0m]',msg.topic,decode[yconfig['chatbot']['mqttparam']])
        #print "DECODE: ", decode
        #print "if: decocechatbotmqttparam: ",decode[yconfig['chatbot']['mqttparam']]
        #print "if the same: ", yconfig['chatbot']['mqttalive']
        # Check if alpha wants us to verifie our existens
        if extract_message(msg.payload,text='show') == yconfig['chatbot']['status']:
        #if decode[yconfig['chatbot']['mqttparam']] ==  yconfig['chatbot']['status']:
            #message = json.dumps({yconfig['chatbot']['mqttparam']: yconfig['chatbot']['mqttalive'], 'id': '0', 'time': time.time()})
            message = create_from_message(msg.payload,'chatbot is alive','chatbot')
            client.publish(send_topic, message)
            logger.debug('on_message - sending repsone to topic [\033[0;32m%s\033[0m]',send_topic)
            logger.debug('on_message - sent response [\033[0;32m%s\033[0m]',msg.payload)
        elif decode[yconfig['chatbot']['mqttparam']] ==  yconfig['chatbot']['stopps'] or decode[yconfig['chatbot']['mqttparam']] == "avslutar" :
            logger.debug('on_message - received [\033[0;31mshutdown\033[0m] from alpha')
            client.disconnect()
            sys.exit(0)
        else:
            bot_response = kernel.respond(decode[yconfig['chatbot']['mqttparam']])
            if bot_response:
                message = create_from_message(msg.payload,bot_response,'chatbot')
            else:
                message = msg.payload
            # Ande remove this below message
            #message = json.dumps({'text': bot_response,'sender': 'stt','id': '0','bounce': '0','time': time.time()})
            client.publish(send_topic, message)
            logger.debug('on_message sent response back to alpha: [\033[0;35m%s\033[0m]', message)
            # IF chat bot reply message is empty. send back original text to alpha "who is the fastest man alive"
            # This would not get an accept in tellstick, but could get a response from wolfram alpha
            # and if not, perhaps it should go to a secondary chatbot !? int the end this will end upp with tts

class chatbot():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/chatbot.pid'
        self.pidfile_timeout = 5

    def run(self):
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(yconfig['mqtt']['host'], yconfig['mqtt']['port'], 60)
        client.loop_forever()


try:
    # Read Configurations yaml config file
    yconfig = readyaml(ymlfile)
except:
    print "Couldnt find ymlfile !?", ymlfile
    sys.exit(1)

if __name__ == '__main__':
    send_topic = yconfig['mqtt']['topic']['chatbot']
    listen_topic = yconfig['chatbot']['mqtttopic']
    numeric_level = getattr(logging, LOGLEVEL, None)
    FORMAT = '%(asctime)-15s %(levelname)s    - %(name)s - %(message)s'
    logging.basicConfig(format=FORMAT,level=numeric_level)
    logger = logging.getLogger('Chatbot')
    logger.debug('  main listen to mqtt topic [\033[0;32m%s\033[0m]',listen_topic)
    logger.debug('  main sends  to mqtt topic [\033[0;32m%s\033[0m]', send_topic)

    # Chatbot Alice
    kernel = aiml.Kernel()
    kernel.learn("../etc/std-alpha.xml")
    kernel.respond("load aiml t")
    if yconfig['bot']['alice']:
        alicekernel = aiml.Kernel()
        alicekernel.learn("../etc/std-alice.xml")
        alicekernel.respond("load aiml alice")

    app = chatbot()
    daemon_runner = runner.DaemonRunner(app)
    try:
        daemon_runner.do_action()
    except LockTimeout:
        logger.warning('main - Couldnt aquire lock on pid')
