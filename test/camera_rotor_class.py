#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf8')


class camera_rotor(object):
    def __init__(self,begin, end):
        self.x_begin = begin
        self.x_end = end
        self.x_middle = self.x_end / 2
        self.x_focus = 0
        # Set last known focus to middle at start.
        self.x_last_focus = self.x_end - self.x_begin
        # If rotation is accepted. This is how much we rotate
        self.x_moves = 0
        # Tolerance procent movement accepted at most.
        # We dont whant the head to rotate to much.
        self.x_tolerance = 20
        # Tolerance pixels movement accepted at most defined by self.x_tolerance %
        self.x_pixel_tolerance = self.whatispercentageofwhole(self.x_tolerance, self.x_end)
        print self.x_pixel_tolerance


    def calculate(self, focus):
        self.x_focus = focus
    

        self.x_last_focus = self.x_focus
        return self.x_moves

    def percentage(self,part, whole):
        return 100 * float(part)/float(whole)

    def whatispercentageofwhole(self,percent, whole):
        return (percent * whole) / 100.0

# 640*400
test = camera_rotor(0,640)
# Input focus
testout = test.calculate(220)
#testout = test.svtoen('hej')
#test.print_translated_message()
#test.entosv("who are you")
print (testout)