# name: sec13_10_prob1.py
# This program reads a file and writes out a new file with the lines
# in reveresed order. Section 13.11 problem 1 from:
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: July 7, 2024


# open the file and copy each line:
fileHandle = open("test.txt", "r")
lineList = fileHandle.readlines()
fileHandle.close()
#print(len(lineList))
newList = [None]*len(lineList) # create a empty array of size equal to lineList
for i in range(len(lineList)): # copies lineList to newList in opposite order
    newList[i] = lineList[len(lineList)-1-i]
    
for each in newList: # displays the lines in the new file
    print(each)

# write the newList to a new file
fileHandle = open("test2.txt", "w")
for each in newList:
    fileHandle.write(each)
fileHandle.close()
