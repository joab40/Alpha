#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import print_function

from googleapiclient.discovery import build
from yandex_translate import YandexTranslate

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class translator(object):
    def __init__(self, key, service_api):
        #creating object
        self.apiservice = service_api
        self.msg = "EMPTY"
        self.msg_reply = "EMPTY"
        if self.apiservice == 'google':
            self.service = build('translate', 'v2',developerKey=key)

        elif self.apiservice == 'yandex':
            self.service = YandexTranslate(key)


    def svtoen(self, msg):
        if self.apiservice == 'google':
            self.msg_reply = self.service.translations().list(
                source='sv',
                target='en',
                q=[msg]
                ).execute()
            returnstr = self.msg_reply['translations'][0]['translatedText']
            return returnstr

        elif self.apiservice == 'yandex':
            msg_reply = self.service.translate(msg, 'sv-en')
            returnstr = msg_reply['text'][0]
            return returnstr

    def entosv(self, msg):
        if self.apiservice == 'google':
            self.msg_reply = self.service.translations().list(
                source='en',
                target='sv',
                q=[msg]
                ).execute()
            return_string = self.msg_reply['translations'][0]['translatedText']
            return return_string
        elif self.apiservice == 'yandex':
            self.msg_reply = self.service.translate(msg, 'en-sv')
            return_string = self.msg_reply['text'][0]
            return return_string

    def input_svtoen(self):
        self.msg = raw_input("Översätt: ")
        self.svtoen(self.msg)


    def print_translated_message(self):
        #print (self.msg_reply)
        #for a in self.msg_reply:
        print (self.msg_reply['translations'][0]['translatedText'])
        #return_string = self.msg_reply['translations'][0]['translatedText']
        #return return_string



#test = translator('api_key','yandex')
#testout = test.svtoen('hej')
#test.print_translated_message()
#test.entosv("who are you")
#print (testout)