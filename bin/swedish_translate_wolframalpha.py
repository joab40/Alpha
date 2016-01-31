#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyvona
import argparse
import yaml
import logging
import sys
import os
import speech_recognition as sr

reload(sys)
sys.setdefaultencoding('utf8')

basepath = os.path.dirname(os.path.abspath(__file__))
ymlfile = basepath + "/../etc/sasha_config.yml"
libpath = basepath + "/../lib/"

if libpath not in sys.path:
        sys.path.insert(1, libpath)

try:
        import translator_class
except ImportError:
        print "libpath could be wrong, please check/verify translator_class in %s: ", libpath
        exit(1)

try:
        import walpha_question_class
except ImportError:
        print "libpath could be wrong, please check/verify walpha_questions_class in %s: ", libpath
        exit(1)


def readyaml(yfile):
    logger.info("readyaml             - read yaml file            [\033[0;32mREAD\033[0m] on admin on host: %s ", yfile)
    # Add check for file exist/read
    with open(yfile, 'r') as f:
        config =  yaml.load(f)
    f.close()
    return config

def alphaquest():

    while True:
        # obtain audio from the microphone
        message = "EMTPY"
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            logger.warning("sasha              - Say Something!            [\033[0;31mWAITING\033[0m] ")

            audio = r.listen(source)

        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            message = r.recognize_google(audio,language="sv-SE")
            print("Google Speech Recognition thinks you said " + message)
            logger.info("sasha think you said  - google speak              [\033[0;32mOK\033[0m] : %s", message)
        except sr.UnknownValueError:
            #print("Google Speech Recognition could not understand audio")
            logger.info("sasha Google SpeechRecognition failed understand  [\033[0;31mFAILED\033[0m] : %s", message)
            #logger.info("sasha think you said  - google speak              [\033[0;32mOK\033[0m] : %s", message)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return message



if __name__ == '__main__':
    Version = "0.01"
    parser = argparse.ArgumentParser(description='alpha')
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
        logger = logging.getLogger('wAlpha')
    logger.debug("__main__: Starting ervers: %s ",Version)
    # Read Configurations yaml config file
    yconfig = readyaml(ymlfile)

    logger.info("main                 - yaml read                 [\033[0;32mOK\033[0m] %s " ,yconfig['pyvonna']['user_key'])
    logger.info("main                 - yaml read                 [\033[0;32mOK\033[0m] %s " ,yconfig['pyvonna']['cert_key'])
    logger.info("main                 - yaml read                 [\033[0;32mOK\033[0m] %s " ,yconfig['translate']['google_api_key'])
    logger.info("main                 - yaml read                 [\033[0;32mOK\033[0m] %s " ,yconfig['wolframalpha']['alpha_api_key'])

    #exit(0)
    v = pyvona.create_voice(yconfig['pyvonna']['user_key'], yconfig['pyvonna']['cert_key'])
    v.voice_name = 'Astrid'
    q_message = alphaquest()
    #print (q_message)
    trans = translator_class.translator(yconfig['translate']['google_api_key'])
    testout = trans.svtoen(q_message)
    print (testout)

    alphao = walpha_question_class.alpha(yconfig['wolframalpha']['alpha_api_key'])
    eanswer = alphao.ask(testout)
    print (eanswer)
    sanswer = trans.entosv(eanswer)

    v.speak(sanswer)


