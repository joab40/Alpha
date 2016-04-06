#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')

basepath = os.path.dirname(os.path.abspath(__file__))
ymlfile = basepath + "/../etc/alpha_config.yml"
libpath = basepath + "/../test/"

if libpath not in sys.path:
        sys.path.insert(1, libpath)

import camera_rotor_class



if __name__ == '__main__':
# 640*400

    test = camera_rotor_class.camera_rotor(0,640)
# Input focus
    testa = test.focus(450)
    testa = test.focus(550)
    testa = test.focus(250)
    testa = test.focus(450)
    testa = test.focus(10)
    testa = test.focus(450)

    #test = test.focus(310)
#testout = test.svtoen('hej')
#test.print_translated_message()
#test.entosv("who are you")
#print (testout)