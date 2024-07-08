# name: alice_words.py
# This program creates a text file names alice_words.txt that contains 
# an alphabetical listing of all words and the number of times they
# occur from a text of alice's adventures in wonderland from 
# http://www.gutenberg.org/
# to complet problem 3 from section 20.8 from:
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: July 7, 2024


def remove_punctuation(s):
    "used to remove punctuation in a string"
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
    return s_sans_punct

def punctuation2space(s):
    """ used instead of the remove_punctuation() function
    because at some cases it would cause concatonation of 2
    words and would also not count words with dashes inbetween
    them as 2 seperate words"""
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~·"
    s_sans_punct = ""
    for letter in s:
        if letter not in punctuation:
            s_sans_punct += letter
        if letter in punctuation: #put a space in place of punctuation
            s_sans_punct += " "
    return s_sans_punct

def remove_numbers(string):
    """ Used to remove all numbers from a string"""
    numbers = "0123456789"
    s_wOutNums = ""
    for char in string:
        if char not in numbers:
            s_wOutNums += char
    return s_wOutNums


# first read the file and copy each line
fileHandle = open("Alices's Adventures in Wonderland.txt", "r")
lineList = fileHandle.readlines()
fileHandle.close()

word_counts = {} # initialize a dictionary to count words

for line in lineList: #parse each line:
    noNumsLine = remove_numbers(line) # remove all numbers as they are not words
    noPuncLine = punctuation2space(noNumsLine)# need to filter all punctuation
    lowerLine = noPuncLine.lower() # need to make all lower case
    tempList = lowerLine.split() #split the line insto a list of words
    
    # now parse tempList to place each word into the dictionary
    # while incrementing the word count
    for word in tempList:
        """ noNumsWord = remove_numbers(word)
        noPuncWord = remove_punctuation(noNumsWord)
        lowerWord = noPuncWord.lower() """
        word_counts[word] = word_counts.get(word, 0) + 1

wordList = list(word_counts.items()) # place into a list format
wordList.sort() #sorts alphabetically

# Create a file named alice_words.txt and print the word counts to it
fileHandle = open("alice_words.txt", "w")
#create the layout
layout = "{0:20}{1:2}"
fileHandle.write(layout.format("Word", "Count"))
fileHandle.write("\n==========================\n")

for each in wordList: # write everthing to a file to show the word count
    fileHandle.write(layout.format(each[0], each[1]))
    fileHandle.write("\n")
fileHandle.close()
