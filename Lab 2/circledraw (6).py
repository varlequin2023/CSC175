#Circle Draw by Vincent Arlequin - FA/24 CSC-175-02 - 09/13/24
#To Do's: Initialize a turtle, draw a circle, fill it with green
#Note: For this solution I have elected to use the longer method of drawing the circle so I can use a for loop and not use the circle() method.

#Importing Turtle Library
import turtle

#Initialize "circle" Turtle
circle = turtle.Turtle()

#Set line and fill color to green
circle.pencolor("green")
circle.fillcolor("green")

#Begins Fill (so that shape can be filled with green)
circle.begin_fill()

#Loop that draws a circle one degree at a time
for i in range(365):
    #Draws a part of the circle
    circle.forward(1)
    #Turns the turtle in preparation for drawing the next part of the circle
    circle.left(1)

#Completes and fills shape
circle.end_fill()
