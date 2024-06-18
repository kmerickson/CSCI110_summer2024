import sys

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
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)

test_suite() #call to run tests