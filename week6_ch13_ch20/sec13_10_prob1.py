# name: sec13_10_prob1.py
# This program reads a file and writes out a new file with the lines
# in reveresed order. Section 13.11 problem 1 from:
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: July 7, 2024



fileHandle = open("test.txt", "r")
lineList = fileHandle.readlines()
fileHandle.close()
print(len(lineList))
newList = [None]*len(lineList)
for i in range(len(lineList)):
    newList[i] = lineList[len(lineList)-1-i]
    
for each in newList:
    print(each)

fileHandle = open("test2.txt", "w")
for each in newList:
    fileHandle.write(each)
fileHandle.close()
