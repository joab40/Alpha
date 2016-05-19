#!/produkter/gnu/python/bin/python
# -*- coding: iso-8859-15 -*-
import unittest
import os
import sys

import lib.readYaml as readYaml

class Testreadyaml(unittest.TestCase):
    def setUp(self):
        pass

    def test_readyaml(self):
        basepath = os.path.dirname(os.path.abspath(__file__))
        pathen=basepath + "/../files/site.xml"
        self.assertEqual(readYaml.readYaml(pathen), 1, "Site not 1!")


if __name__ == '__main__':

