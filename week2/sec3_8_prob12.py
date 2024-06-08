# name: sec3_8_prob12
# purpose: create a clock face from turtles as shown in section 3.8, problem 12
#   from http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
# author: Keegan Erickson
# date created: 6/8/24


import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("lightgreen")    # changes the background color

bob = turtle.Turtle()    # Create a turtle named bob
bob.color("blue")       # make bob blue
bob.shape("turtle")     # make the turtle named bob look like a turtle

for i in range(12): # create a for loop that iterates 12 times (it was too painful to hard code)
    bob.penup() # makes bob fly so that he doesn't leave tracks
    bob.left(30)    # rotates bob left 30 degrees
    bob.forward(150)    # moves bob forward
    bob.pendown()   # puts bob on the ground so that he leaves tracks
    bob.forward(15)
    bob.penup()
    bob.forward(25)
    bob.stamp() # bob stamps his shape down
    bob.goto(0,0)   # moves bob back to the center

wn.mainloop()             # Wait for user to close window