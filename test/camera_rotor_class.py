#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')


class camera_rotor(object):
    def __init__(self,begin, end):
        self.x_begin = begin
        self.x_end = end
        self.x_middle = self.x_end / 2
        self.x_focus = 0
        # Set last known focus to middle at start. that initiated a movement
        self.x_last_focus = self.x_end - self.x_begin
        # If rotation is accepted. This is how much we rotate
        self.x_moves = 0
        # Tolerance procent movement accepted at most.
        # We dont whant the head to rotate to much.
        self.x_tolerance = 20
        # Tolerance pixels movement accepted at most defined by self.x_tolerance %
        self.x_pixel_tolerance = self.whatispercentageofwhole(self.x_tolerance, self.x_end)

        # Zones
        self.cam_zones = 5
        # Center zone to middle
        self.cam_zone = 3
        # ex 640 / 5
        self.cam_zone_sizes = self.x_end / self.cam_zones
        # SERVOBLASTER
        self.servo_middle = 50
        self.servo_focus = self.servo_middle
        self.servo_zone_sizes = 100 / self.cam_zones


        #print self.x_pixel_tolerance

    def camrotate(self):
        print "test"

    def focus(self, xfocus):
        self.x_focus = xfocus
        self.x_last_focus = self.x_focus
        print self.cam_zone_sizes
        self.findzone()
        self.move_servo_to_zone()
        return self.x_moves

    def findzone(self):
        print "zone"
        select_xone = 1
        while select_xone <= self.cam_zones:
            #print "debug ", self.x_focus, select_xone, self.cam_zone_sizes, select_xone * self.cam_zone_sizes
            if self.x_focus < select_xone * self.cam_zone_sizes:
                print "Found zone ", select_xone
                self.cam_zone = select_xone
                break
            select_xone += 1

    def move_servo_to_zone(self):
        print "DEBUG: servo precent focus: ", self.servo_focus
        print "DEBUG: Move servo to: ", self.servo_zone_sizes * self.cam_zone - (self.servo_zone_sizes / 2)


    def percentage(self,part, whole):
        return 100 * float(part)/float(whole)

    def whatispercentageofwhole(self,percent, whole):
        return (percent * whole) / 100.0

# 640*400
#test = camera_rotor(0,640)
# Input focus
#testout = test.calculate(450)
#testout = test.svtoen('hej')
#test.print_translated_message()
#test.entosv("who are you")
#print (testout)