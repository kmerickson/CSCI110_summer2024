# name: sec11_22_prob10.py
# Shows function replace(s, old, new) that replaces all occurrences 
# of old with new in a string s. From sec 11.22, prob 10 from:
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: June 30, 2024

import string
import sys


def isSameChar(a, b):
    """ gives a bool telling a two chars are the same"""
    if a == b:
        return True 
    else:
        return False


def replace(s, old, new):
    """ searches through a string for an old char or str and replaces 
    them with a new one """
    #break apart the str, old, and new
    sList = list(s)
    sLen = len(sList)
    oldList = list(old)
    oldLen = len(oldList)
    oldLastChar = oldList[oldLen-1]
    newList = list(new)
    newLen = len(newList)
    newLastChar = newList[newLen-1]

    print(s)
    # search string for an old string to replace
    # look for first item in old string
    for i in range(sLen):
        #print("sList[i]: ", sList[i], ", oldList[0]: ", oldList[0])
        if isSameChar(sList[i], oldList[0]):
            remLen = oldLen
            #print("Same char found!")
            checks = [False]*oldLen
            for j in range(oldLen): #check following list items if all chars match
                #print("j: ", j)
                if oldList[j] == sList[i+j]:
                    checks[j] = True
                else:
                    matchFound = False
                FalseCount = checks.count(False)
                #print("False checks count = ", FalseCount)
            # replace characters in list
            if FalseCount == 0:
                t = i+oldLen
                if t > sLen:
                    sList[i] = []
                    sList[i] = newList
                else:
                    #sList[i:t] = []
                    sList[i:i] = newList
                    sList[t:t+oldLen] = []
                    #print("made it here")

    #print(sList)
    newS = "".join(sList)
    print(newS)
    return newS


def test(did_pass):
    """ Print the results of a test. """
    linenum = sys._getframe(1).f_lineno # get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} Failed.".format(linenum))
    print(msg)

def test_suite():
    test(replace("Mississippi", "i", "I") == "MIssIssIppI")

    s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
    test(replace(s, "om", "am") ==
        "I love spam! Spam is my favorite food. Spam, spam, yum!")

    test(replace(s, "o", "a") ==
        "I lave spam! Spam is my favarite faad. Spam, spam, yum!")

test_suite()