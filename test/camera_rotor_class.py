#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

reload(sys)
sys.setdefaultencoding('utf8')


class camera_rotor(object):
    def __init__(self,begin, end,camangle,servoangle,camzones):
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
        self.cam_zones = camzones
        # Center zone to middle
        self.cam_zone_middle = ( self.cam_zones + 1 ) / 2
        self.cam_zone = self.cam_zone_middle
        self.cam_last_known_zone = self.cam_zone
        # ex 640 / 5
        self.cam_zone_sizes = self.x_end / self.cam_zones
        # SERVOBLASTER
        self.servo_middle = 50
        self.servo_focus = self.servo_middle
        self.servo_last_known_focus = self.servo_focus
        self.servo_zone_sizes = 100 / self.cam_zones
        # Prevent servo to rotate more or less 0%-100%
        self.servo_cam_focus_zone_procent = 50
        print "cam zone sizes: ",self.cam_zone_sizes
        print "print: ", camangle, servoangle
        self.servo_step_procent =  float(camangle) / float(servoangle) / camzones * 100

        #print self.x_pixel_tolerance

    def camrotate(self):
        print "test"

    def focus(self, xfocus):
        self.x_focus = xfocus
        self.x_last_focus = self.x_focus

        self.in_the_zone = self.findzone()
        if self.in_the_zone is not self.cam_zone_middle:
            print "FOCUS: servo procent RANGE/TOTAL/STATUS position : ", self.servo_cam_focus_zone_procent
            self.x_moves = self.move_servo_to_zone()
        else:
            print "FOCUS: dont move servomotor: ", self.cam_zone_middle
            print "FOCUS: servo procent RANGE/TOTAL/STATUS position : ", self.servo_cam_focus_zone_procent
            self.x_moves = 0

        return self.x_moves

    def findzone(self):
        #print "zone"
        select_xone = 1
        while select_xone <= self.cam_zones:
            #print "debug ", self.x_focus, select_xone, self.cam_zone_sizes, select_xone * self.cam_zone_sizes
            if self.x_focus < select_xone * self.cam_zone_sizes:
                print "findzone: FOUND zone(!): ", select_xone, self.x_focus
                self.cam_zone = select_xone
                return select_xone
                break
            select_xone += 1

    def move_servo_to_zone(self):
        print "move_servo_to_zone: AT THIS MOMENT : servo precent focus: ", self.servo_cam_focus_zone_procent
        #print "move_servo_to_zone: Move servo to: ", self.servo_zone_sizes * self.cam_zone - (self.servo_zone_sizes / 2)
        #print "procent movement: ",
        multiple_movement = abs(self.cam_last_known_zone - self.cam_zone)
        print "cam last known zone: ", self.cam_last_known_zone, " zone know: ", self.cam_zone, " multiple MOVEMENTS: ", multiple_movement
        if self.cam_last_known_zone > self.cam_zone and self.servo_cam_focus_zone_procent > 15:
            print "<---- LEFT: ", self.cam_last_known_zone, self.cam_zone
            print "servo_cam_focus_zone_procent: ", self.servo_cam_focus_zone_procent
            self.servo_cam_focus_zone_procent -= self.servo_step_procent * multiple_movement
            print "step left 10%", self.servo_cam_focus_zone_procent
            self.cam_last_known_zone = self.cam_zone_middle
            print "DONE LEFT"
            print ""
            return self.servo_cam_focus_zone_procent
        elif self.cam_last_known_zone < self.cam_zone and self.servo_cam_focus_zone_procent < 85:
            print "------> RIGHT: ", self.cam_last_known_zone, self.cam_zone
            print "servo_cam_focus_zone_procent: ", self.servo_cam_focus_zone_procent
            self.servo_cam_focus_zone_procent += self.servo_step_procent * multiple_movement
            print "stepping right 10%", self.servo_cam_focus_zone_procent
            self.cam_last_known_zone = self.cam_zone_middle
            print "DONE RIGH"
            print ""
            return self.servo_cam_focus_zone_procent
        #self.cam_last_known_zone = self.cam_zone



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