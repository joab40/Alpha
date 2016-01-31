#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

#__author__ = ' (Joe Gregorio)'

from googleapiclient.discovery import build

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class translator(object):
    def __init__(self, key):
        #creating object
        self.msg = "EMPTY"
        self.msg_reply = "EMPTY"

        self.service = build('translate', 'v2',
            developerKey=key)

    def svtoen(self, msg):
        self.msg_reply = self.service.translations().list(
                source='sv',
                target='en',
                q=[msg]
            ).execute()
        self.r_str = self.msg_reply['translations'][0]['translatedText']
        return (self.r_str)

    def entosv(self, msg):
        self.msg_reply = self.service.translations().list(
                source='en',
                target='sv',
                q=[msg]
            ).execute()
        return_string = self.msg_reply['translations'][0]['translatedText']
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



#test = translator('Google_API_KEY')
#testout = test.svtoen('hej')
#test.print_translated_message()
#test.svtoen("hej då")
#print (testout)