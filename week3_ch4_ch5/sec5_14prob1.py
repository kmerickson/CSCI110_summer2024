# name: sec5_14prob1.property
# Assume the days of the week are numbered 0,1,2,3,4,5,6 from 
# Sunday to Saturday. This script shows  a function which is 
# given the day number, and it returns the day name (a string).
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# for problem 1 in section 5.14
# author: Keegan Erickson
# date: June 10, 2024


def dayOfWeek(n):
    if n == 0:
        d = "Sunday"
    elif n == 1:
        d = "Monday"
    elif n == 2:
        d = "Tuesday"
    elif n == 3:
        d = "Wednesday"
    elif n == 4:
        d = "Thursday"
    elif n == 5:
        d = "Friday"
    elif n == 6:
        d = "Saturday"
    else:
        d = "That is not a valid entry."

    return d

n = input("Please type in a number, 0-6, to represent a day of the week: ")
n = int(n)

s = dayOfWeek(n)
print(s)

