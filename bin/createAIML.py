#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# ./islay_of_mist.py -d INFO -i g700 -c STATUS

import logging
import argparse
import time
import commands
import sys
import os
import yaml
import re


basepath = os.path.dirname(os.path.abspath(__file__))

ymlfile = basepath + "/../etc/islandcontrol.yml"

libpath = basepath + "/../lib/"

if libpath not in sys.path:
        sys.path.insert(1, libpath)

file_template = []
pattern_list = []

def create_template_header():
    file_template.append('<aiml version="1.0.1" encoding="UTF-8">')
    file_template.append('<!-- basic_chat.aiml -->')

def create_template_ending():
    file_template.append('</aiml>')

def create_template_category(pattern,alicesays):
    file_template.append('    <category>')
    file_template.append('        <pattern>' + pattern + '</pattern>')
    file_template.append('        <template>')
    file_template.append('            ' + alicesays)
    file_template.append('        </template>')
    file_template.append('    </category>')


def create_aiml_file(fil,alicesays):
    file = open(fil, 'w')
    file.truncate()
    create_template_header()

    yesorno = raw_input("Do you want to add a entry [yes|no]: ")
    while yesorno == 'yes' or yesorno == 'y' or yesorno == '':
        pattern = raw_input("pattern: ")
        pattern_list.append(pattern)
        iasays_tmp = raw_input("Alice says [" + alicesays + "]: ")
        if iasays_tmp:
            alicesays = iasays_tmp
        pattern = pattern.upper()
        create_template_category(pattern,alicesays)

        yesorno = raw_input("Add another pattern? [yes|no: ]")
        os.system('clear')
        print ""
        for pat in pattern_list:
            print pat
        print ""

    create_template_ending()

    for tmp in file_template:
        print tmp


    for row in file_template:
        file.write(row + '\n')



if __name__ == '__main__':
    Version = '0.01'

    parser = argparse.ArgumentParser(description='Islay Of Mist')

    parser.add_argument('-d', '--loglevel',default='', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL' ], help='Default WARNING')
    parser.add_argument('-f', '--logfile', default='', help='Path to Logfile')
    args = parser.parse_args()


    filename = raw_input("Name of file: ")
    alicesays = raw_input("Alice says : ")

    ssh_alias_config = filename
    create_aiml_file(filename,alicesays)


