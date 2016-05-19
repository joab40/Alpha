#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml
import sys


#reload(sys)
#sys.setdefaultencoding('utf8')

basepath = os.path.dirname(os.path.abspath(__file__))
ymlfile = basepath + "/../etc/alpha_config.yml"
libpath = basepath + "/../lib/"

if libpath not in sys.path:
        sys.path.insert(1, libpath)

# Topic wildcard
topic = "alpha/#"

def readyaml(yfile):
    """ Read yaml file

    :param yfile:
    :return:
    """
    #logger.info("readyaml             - read yaml file            [\033[0;32mREAD\033[0m] on admin on host: %s ", yfile)
    # Add check for file exist/read
    with open(yfile, 'r') as f:
        config = yaml.load(f)
    f.close()
    return config
