#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:17:42 2018

@author: thomas
"""

import echecs
import unittest

class TestEchecs(unittest.TestCase):
    def testMultiply(self):
        a = 3
        b = 4
        expected = 12
        actual = echecs.multiply(a,b)
        self.assertEqual(expected, actual,"failed test for 3x4")
        

if __name__ == '__main__':
   log_file = 'testResults.txt'
   f = open(log_file, "w")
   runner = unittest.TextTestRunner(f)
   unittest.main(testRunner=runner)
   f.close()