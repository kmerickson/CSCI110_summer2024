# name: sec7_26_prob9.py
# Creates a function to_print the first n number triangle numbers from
# section 7.26 problem 9 or the website
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: June 17, 2024

def print_triangle_numbers(n):
    temp = 0
    for i in range(n):
        j = i + 1
        if j == 1:
            print(1, "\t", 1)
            triangle = 1
        else:
            triangle = j + temp
            print(j, "\t", triangle)
        temp = triangle
    

n = input("Please input a number to list all of the triangle numbers leading up to it: ")
n = int(n)
print()
print_triangle_numbers(n)
print()

