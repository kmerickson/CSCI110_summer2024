import string
import sys


def isSameChar(a, b):
    """ gives a bool telling a two chars are the same"""
    if a == b:
        return True 
    else:
        return False

def checkLongEnough(s1, s2, i):
    s1Len = len(s1)
    s2Len = len(s2)
    s2LastChar = s2[s2Len-1]
    if len(s1[i-s2Len:i]) >= s2Len:
        return True
    else: 
        return False

#print(checkLongEnough("mississippi", "ssiss", 3))

def replace(s, old, new):
    """ searches through a string for an old char or str and replaces 
    them with a new one """
    #break a part the str, old, and new
    sList = list(s)
    sLen = len(sList)
    oldList = list(old)
    oldLen = len(oldList)
    oldLastChar = oldList[oldLen-1]
    newList = list(new)
    newLen = len(newList)

    
#replace(s, "i", "I")
s = "mississippi"
m = list(s)
print(m.index('s',2))