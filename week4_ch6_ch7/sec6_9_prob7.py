# name: sec6_9_prob7.py
# Creates a function to_secs that converts hours, minutes and seconds
# to a total number of seconds, from pronlem 7 of sec 6.9 of
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: June 17, 2024

import sys

def to_secs( hour, min, sec):
    min = hour * 60 + min
    sec = sec + min*60
    return sec

def absolute_value(x):
    if x < 0:
        return -x
    else: 
        return x

def test(did_pass):
    """ Print the results of a test. """
    linenum = sys._getframe(1).f_lineno # get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} Failed.".format(linenum))
    print(msg)

def test_suite():
    """ Run the test suite for code in this module (this file)."""
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)



test_suite() #call to run tests