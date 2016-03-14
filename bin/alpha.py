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

try:
        import translator_class
except ImportError:
        print "libpath could be wrong, please check/verify translator_class in %s: ", libpath
        exit(1)


def readyaml(yfile):
    logger.info("readyaml             - read yaml file            [\033[0;32mREAD\033[0m] on admin on host: %s ", yfile)
    # Add check for file exist/read
    with open(yfile, 'r') as f:
        config =  yaml.load(f)
    f.close()
    return config

def run_sasha(onlytextoption,onlytexttospeech):

    while True:
        # obtain audio from the microphone
        message = "EMTPY"
        if onlytextoption or onlytexttospeech:
            piled.on('green')
            message = raw_input("Talk To Alpha: ")
            piled.off()

        else:
            r = sr.Recognizer()
            # Ubuntu Linux default soundcard and MIC
            # with sr.Microphone() as source:
            # RaspberryPi default soundcard 0 and Usb MIC 3
            with sr.Microphone(device_index = 3, sample_rate = 16000, chunk_size = 1024) as source:
                print("Say something!")
                logger.warning("sasha              - Say Something!            [\033[0;31mWAITING\033[0m] ")

                audio = r.listen(source)

            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                message = r.recognize_google(audio,language="sv-SE")
                piled.on('green')
                piled.off()
                print("Google Speech Recognition thinks you said " + message)
                logger.info("sasha think you said  - google speak              [\033[0;32mOK\033[0m] : %s", message)
            except sr.UnknownValueError:
                piled.on('red')
                piled.off()
                #print("Google Speech Recognition could not understand audio")
                logger.info("sasha Google SpeechRecognition failed understand  [\033[0;31mFAILED\033[0m] : %s", message)
                #logger.info("sasha think you said  - google speak              [\033[0;32mOK\033[0m] : %s", message)
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                piled.on('red')
                piled.off()

        if message == "avsluta":
            piled.off()
            exit()
        elif message == "save":
            kernel.saveBrain("bot_brain.brn")
        else:
            bot_response = kernel.respond(message)
            #print "sasha: ",bot_response
            if not bot_response:
                if yconfig['bot']['alice']:
                    if yconfig['bot']['translate']:
                        message = translate.svtoen(message)
                        print "Meddelande på engelska: ", message

                    bot_response = alicekernel.respond(message)
                    if bot_response:
                        if yconfig['bot']['translate']:
                            print "alice says", bot_response
                            bot_response = translate.entosv(bot_response)
                            print "alice säger: ", bot_response

            if bot_response:
                try:
                    tellstick_cmd = yconfig['tellstick'][bot_response]
                except KeyError, e:
                    logger.info("main                 - verify tellstick          [\033[0;31mFAILED\033[0m] %s: ",str(e))
                else:
                    logger.info("main                 - found tellstick command   [\033[0;32mOK\033[0m] %s: ",tellstick_cmd)
                    status, text = getstatusoutput(yconfig['tellstick'][bot_response])
                    if status == 0:
                        print "OK: ", text
                    else:
                        print "failed: ",status

                if onlytextoption:
                        piled.on('yellow')
                        print "Alpha says: ", bot_response
                        time.sleep(0.5)
                        piled.off()
                else:
                        #os.system(ESPEAK + '"' + bot_response + '"')
                        piled.on('yellow')
                        v.speak(bot_response)
                        time.sleep(0.5)
                        piled.off()
                # Do something with bot_response


if __name__ == '__main__':
        Version = "0.01"
        parser = argparse.ArgumentParser(description='sasha')
        parser.add_argument("--textonly", "-t", help="Text only, disable all voice", action="store_true")
        parser.add_argument("--ttsonly", "-s", help="Text only, disable all voice", action="store_true")
        parser.add_argument('-d', '--loglevel',default='', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL' ], help='Default WARNING')
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

        logger.info("main                 - yaml read                 [\033[0;32mOK\033[0m] %s " ,yconfig['pyvonna']['user_key'])
        logger.info("main                 - yaml read                 [\033[0;32mOK\033[0m] %s " ,yconfig['pyvonna']['cert_key'])


        # Create the kernel and learn AIML files
        kernel = aiml.Kernel()


        kernel.learn("../etc/std-alpha.xml")
        kernel.respond("load aiml t")
        if yconfig['bot']['alice']:
            alicekernel = aiml.Kernel()
            alicekernel.learn("../etc/std-alice.xml")
            alicekernel.respond("load aiml alice")
            if yconfig['bot']['translate']:

                translate = translator_class.translator(yconfig['translate']['api_key'],yconfig['translate']['service'])

        ESPEAK = "/usr/bin/espeak -v swedish "
        ONTELLSTICKTEST = "ssh life " + "'" + "/usr/bin/tdtool --on vardagsrum" + "'"
        OFFTELLSTICKTEST = "ssh life " + "'" + "/usr/bin/tdtool --off vardagsrum" + "'"
        TELLSTICKTEMP =  "ssh life /usr/local/bin/temperatur.sh"

        if not args.textonly:
            v = pyvona.create_voice(yconfig['pyvonna']['user_key'], yconfig['pyvonna']['cert_key'])
            v.voice_name = 'Astrid'
        piled = led_class.led()
        #piled.on('blue')
        #time.sleep(1)
        #piled.off()

        run_sasha(args.textonly,args.ttsonly)
