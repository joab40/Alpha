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

    test = camera_rotor_class.camera_rotor(0,640,75,180,5)
# Input focus
    testa = test.focus(450)
    print (testa)
    testa = test.focus(550)
    print (testa)
    testa = test.focus(320)
    print (testa)
    testa = test.focus(220)
    print (testa)
    testa = test.focus(210)
    print (testa)
    exit(0)
    testa = test.focus(180)
    print (testa)
    testa = test.focus(160)
    print (testa)
    testa = test.focus(140)
    print (testa)
    testa = test.focus(100)
    print (testa)
    testa = test.focus(50)
    print (testa)
    testa = test.focus(320)
    print (testa)
    testa = test.focus(320)
    print (testa)
    testa = test.focus(320)
    print (testa)
    testa = test.focus(450)
    print (testa)
    testa = test.focus(450)
    print (testa)
    testa = test.focus(450)
    print (testa)
    testa = test.focus(220)
    print (testa)
    testa = test.focus(210)
    print (testa)
    testa = test.focus(180)
    print (testa)
    testa = test.focus(160)
    print (testa)
    testa = test.focus(140)
    print (testa)
    testa = test.focus(100)
    print (testa)
    testa = test.focus(550)

    #testa = test.focus(320)
    #testa = test.focus(320)

    #test = test.focus(310)
#testout = test.svtoen('hej')
#test.print_translated_message()
#test.entosv("who are you")
    print (testa)