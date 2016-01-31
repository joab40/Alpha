#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
        import wolframalpha
except ImportError:
        print 'You need wolframalpha in %s ',libpath
        sys.exit(1)


import sys

reload(sys)
sys.setdefaultencoding('utf8')


class alpha(object):
    def __init__(self, key):
        #creating object
        self.client = wolframalpha.Client(key)

    def ask(self, msg):
        self.res = self.client.query(msg)
        return self.res.pods[1].text

    def input_ask(self):
        self.msg = raw_input("What is your question? ")
        self.ask(self.msg)
        self.print_message()

    def print_message(self):
        print self.res.pods[1].text

#test = alpha('WOLFRAMALPHA_API_KEY')
#test.ask('who is the fastest runner on earth')
#test.input_ask()
#test.print_message()