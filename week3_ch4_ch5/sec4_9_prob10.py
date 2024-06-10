# name: sec4_9_prob10.property
# this python script creates a image shown as directed by exercise
# 10 in section 4.9 of 
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: June 9, 2024
import turtle

sideLen = 100
angle = 144
spacing = 350

wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Section 4.9 exercise 10")
bob = turtle.Turtle() 
bob.color("green")    
bob.pensize(3)
bob.speed(0)

def drawStar(t, sz):
    """input a turtle object and a size for the length of the star"""
    for i in range(5):
        t.forward(sz)
        t.right(144)

for i in range(5):
    drawStar(bob, sideLen)
    bob.penup()
    bob.forward(spacing)
    bob.right(angle)
    bob.pendown()

wn.mainloop()