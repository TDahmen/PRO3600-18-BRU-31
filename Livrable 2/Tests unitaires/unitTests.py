#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:17:42 2018

@author: thomas
"""

import echecsTest
import unittest

class TestEchecs(unittest.TestCase):
    
    def testValeursAccesiblesPions(self):
        echecsTest.plateau[6][6]=1
        expected=[(5,6)]
        actual=echecsTest.valeurs_accessibles(6,6)
        self.assertEqual(expected,actual,"failed test for pion")
        
    def testValeursAccesiblesCavaliers(self):
        echecsTest.plateau[6][6]=2
        expected=[(5,4),(4,5),(4,7),(5,8),(7,4),(7,8),(8,5),(8,7)]
        actual=echecsTest.valeurs_accessibles(6,6)
        expected.sort()
        actual.sort()
        self.assertEqual(expected,actual,"failed test for cavalier")
        
    def testValeursAccesiblesFous(self):
        echecsTest.plateau[6][6]=3
        expected=[(5,5),(4,4),(3,3),(2,2),(7,7),(8,8),(9,9),(7,5),(8,4),(9,3),(5,7),(4,8),(3,9)]
        actual=echecsTest.valeurs_accessibles(6,6)
        expected.sort()
        actual.sort()
        self.assertEqual(expected,actual,"failed test for fous")
    
    def testValeursAccesiblesTours(self):
        echecsTest.plateau[6][6]=4
        expected=[(5,6),(4,6),(3,6),(2,6),(6,2),(6,3),(6,4),(6,5),(6,7),(6,8),(6,9),(7,6),(8,6),(9,6)]
        actual=echecsTest.valeurs_accessibles(6,6)
        expected.sort()
        actual.sort()
        self.assertEqual(expected,actual,"failed test for tours")
    
    def testValeursAccessiblesReines(self):
        echecsTest.plateau[6][6]=5
        expected=[(5,6),(4,6),(3,6),(2,6),(6,2),(6,3),(6,4),(6,5),(6,7),(6,8),(6,9),(7,6),(8,6),(9,6),(5,5),(4,4),(3,3),(2,2),(7,7),(8,8),(9,9),(7,5),(8,4),(9,3),(5,7),(4,8),(3,9)]
        actual=echecsTest.valeurs_accessibles(6,6)
        expected.sort()
        actual.sort()
        self.assertEqual(expected,actual,"failed test for reines")
        
    def testValeursAccessiblesRois(self):
        echecsTest.plateau[6][6]=6
        expected=[(5,5),(5,6),(5,7),(6,5),(6,7),(7,5),(7,6),(7,7)]
        actual=echecsTest.valeurs_accessibles(6,6)
        expected.sort()
        actual.sort()
        self.assertEqual(expected,actual,"failed test for rois")

if __name__ == '__main__':
   log_file = 'testResults.txt'
   f = open(log_file, "w")
   runner = unittest.TextTestRunner(f)
   unittest.main(testRunner=runner)
   f.close()
   
