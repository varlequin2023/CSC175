#Pentagon Draw by Vincent Arlequin - FA/24 CSC-175-02 - 09/13/24
#To Do's: Initialize a turtle, Draw a pentagon, fill interior with red.

#Importing Turtle Library
import turtle

#Initialize "pentagon" Turtle
pentagon = turtle.Turtle()

#Set line and fill colors to red
pentagon.pencolor("red")
pentagon.fillcolor("red")

#Begins Fill (so that shape can be filled with red)
pentagon.begin_fill()

#Loop that repeats drawing the necessary lines for a drawing the pentagon
for i in range(5):
    #Draws a 50 unit line
    pentagon.forward(50)
    #Turns the turtle in preparation for drawing the next line
    pentagon.left(72)

#Completes and fills shape
pentagon.end_fill()
