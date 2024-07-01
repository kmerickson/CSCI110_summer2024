# name: sec8_19_prob5.py
# Assigns a set of text to a variable in your program a triple-quoted 
# string that contains the poem if by rudyard kipling, this program
# has a function which removes all punctuation from the string, breaks 
# the string into a list of words, and counts the number of words in 
# your text that contain the letter “e”, and prints an analysis of 
# the text. From section 8.19 problem 5 of:
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: June 30, 2024

import string

ifPoem = """
If you can keep your head when all about you   
    Are losing theirs and blaming it on you,   
If you can trust yourself when all men doubt you,
    But make allowance for their doubting too;   
If you can wait and not be tired by waiting,
    Or being lied about, don’t deal in lies,
Or being hated, don’t give way to hating,
    And yet don’t look too good, nor talk too wise:

If you can dream—and not make dreams your master;   
    If you can think and not make thoughts your aim;   
If you can meet with Triumph and Disaster
    And treat those two impostors just the same;   
If you can bear to hear the truth you’ve spoken
    Twisted by knaves to make a trap for fools,
Or watch the things you gave your life to, broken,
    And stoop and build ’em up with worn-out tools:

If you can make one heap of all your winnings
    And risk it on one turn of pitch-and-toss,
And lose, and start again at your beginnings
    And never breathe a word about your loss;
If you can force your heart and nerve and sinew
    To serve your turn long after they are gone,   
And so hold on when there is nothing in you
    Except the Will which says to them: ‘Hold on!’

If you can talk with crowds and keep your virtue,   
    Or walk with Kings nor lose the common touch,
If neither foes nor loving friends can hurt you,
    If all men count with you, but none too much;
If you can fill the unforgiving minute
    With sixty seconds’ worth of distance run,   
Yours is the Earth and everything that’s in it,   
    And which is more you’ll be a Man, my son!
"""



# remove all punctuation from string
def remove_punctuation(s):
    s_noPunct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_noPunct += letter
    #print(s_noPunct)
    return s_noPunct



# give a bool telling if an 'e' char is present in a string
def isThere_e(str):
    for i in str:
        if i == 'e':
            return True
    return False

def count_let_e(text):
    remove_punctuation(text)

    #  break into a list of words
    wordList= remove_punctuation(ifPoem).split()
    #print(new_s)

    e_count = 0
    #check each word if e is present and take a count
    for each in wordList:
        if isThere_e(each):
            e_count = e_count + 1
    
    wordCount = len(wordList)
    eWord_percent = (e_count / wordCount) * 100

    output = "Your text contains {0} words, of which {1} ({2:.2f}%) contain an 'e' character.".format(wordCount, e_count, eWord_percent)
    print()
    print(output)
    print()
    
    

count_let_e(ifPoem)










