#!/usr/bin/python
import time
import paho.mqtt.client as mqtt
import json
from daemon import runner
import yaml
import os,sys
import logging
from lockfile import LockTimeout


basepath = os.path.dirname(os.path.abspath(__file__))
ymlfile = basepath + "/../etc/alpha_config.yml"
libpath = basepath + "/../lib/"
LOGLEVEL = 'DEBUG'


if libpath not in sys.path:
        sys.path.insert(1, libpath)

from messager_mqtt import create_message,extract_message,create_from_message,bounche_message

def readyaml(yfile):
    with open(yfile, 'r') as f:
        config =  yaml.load(f)
    f.close()
    return config

def on_connect(client, userdata, rc):
        client.subscribe(listen_topic)

def on_message(client, userdata, msg):

        decode = json.loads(msg.payload)
        logger.debug('  on_message - from [\033[0;32m%s\033[0m] decode json  [\033[0;32m%s\033[0m]',msg.topic,decode[yconfig[module_name]['mqttparam']])

        if extract_message(msg.payload,text='show') == yconfig[module_name]['status']:
            message = create_from_message(msg.payload,module_name + ' is alive',module_name)
            client.publish(send_topic, message)
            logger.debug('on_message - sending repsone to topic [\033[0;32m%s\033[0m]',send_topic)
            logger.debug('on_message - sent response [\033[0;32m%s\033[0m]',msg.payload)
        elif decode[yconfig[module_name]['mqttparam']] ==  yconfig[module_name]['stopps'] or decode[yconfig[module_name]['mqttparam']] == "avslutar":
            logger.debug('on_message - received [\033[0;31mshutdown\033[0m] from alpha')
            client.disconnect()
            sys.exit(0)
        else:
             logger.debug('on_message lets try to change channels on TV')
             message = create_from_message(msg.payload, 'change tv channel', module_name)
             client.publish(send_topic, message)

class module():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = '/tmp/' + module_name + '.pid'
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
    module_name,end = os.path.basename(sys.argv[0]).split('.')
    send_topic = yconfig['mqtt']['topic'][module_name]
    listen_topic = yconfig[module_name]['mqtttopic']
    numeric_level = getattr(logging, LOGLEVEL, None)
    FORMAT = '%(asctime)-15s %(levelname)s    - %(name)s - %(message)s'
    logging.basicConfig(format=FORMAT,level=numeric_level)
    logger = logging.getLogger(module_name)
    logger.debug('  main listen to mqtt topic [\033[0;32m%s\033[0m]',listen_topic)
    logger.debug('  main sends  to mqtt topic [\033[0;32m%s\033[0m]', send_topic)

    app = module()
    daemon_runner = runner.DaemonRunner(app)
    try:
        daemon_runner.do_action()
    except LockTimeout:
        logger.warning('main - Couldnt aquire lock on pid')
