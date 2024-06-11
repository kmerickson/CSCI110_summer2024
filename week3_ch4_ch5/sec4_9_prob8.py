# name: sec5_14prob8.property
# purpose: Modifies a bar chart script to change the color of the
# bars depending on a range of values of the bar, sec 5.14, prob 8
# http://openbookproject.net/thinkcs/python/english3e/functions.html
# author: Keegan Erickson
# date: June 11, 2024
import turtle 

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()           # Added this line
    t.left(90)
    t.forward(height)
    t.write("  "+ str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    c = assignColor(height)
    t.color("blue", c)
    t.end_fill()             # Added this line
    t.forward(10)

def assignColor(a):
    if a >= 200:
        c = "red"
    elif 100 <= a <= 200:
        c = "yellow"
    elif a < 100:
        c = "green"

    return c

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

xs = [48,117,200,240,160,260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()