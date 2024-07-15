# name: sec19_1_p1.py
# This program implements a function readposint() that uses the input
# dialog to prompt the user for a positive int and checks input to 
# confirm that it meets requirements. it should be able to handle
# inputs that cant converty to int as well as neg ints and edge cases 
# like when the user closes the dialog does not enter anything
# from section 19.6, problem 1 of: 
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: July 7, 2024

def readposint(a):
    """takes input dialog to prompt the user for for a positive 
    integer then checks to confirm the requirements."""
    
    try :
        b = int(a) + 1
        if a < 0:
            print("{0} is not a positive number".format(a))
        elif a == 0:
            print("0 is not a positive integer")
        else:
            print("{0} is a positive integer".format(a))
    except:
        inputError = TypeError("That is not an integer")
        #raise inputError
        print(inputError)
    
    


 
v = input("Please input a positive integer: ")
readposint(v)