# name: sec4_9_prob2.property
# this python script creates a image shown as directed by exercise
# 2 in section 4.9 of 
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: June 9, 2024

import turtle

width = 20
spacing = 10

def draw_square(turt, size):
    """Make turtle t draw a square of sz."""
    for i in range(4):
        turt.forward(size)
        turt.left(90)


wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Section 4.9 exercise 2")
bob = turtle.Turtle() 
bob.color("hotpink")    
bob.pensize(3)

for i in range(5):
    draw_square(bob, width)     # Call the function to draw the square
    bob.penup()
    bob.right(90)
    bob.forward(spacing)
    bob.right(90)
    bob.forward(spacing)
    bob.right(180)
    width = width + 20
    bob.pendown()


wn.mainloop()