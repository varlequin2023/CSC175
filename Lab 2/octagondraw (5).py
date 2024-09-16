#Octagon Draw by Vincent Arlequin - FA/24 CSC-175-02 - 09/13/24
#To Do's: Initialize a turtle, Draw an octogon with a dot at each vertex.

#Importing Turtle Library
import turtle

#Initialize "octagon" Turtle
octagon = turtle.Turtle()

#Set line color to black
octagon.pencolor("black")

#Loop that repeats drawing the necessary lines for drawing the octagon
for i in range(8):
    #Draws a 50 unit line
    octagon.forward(50)
    #Adds a dot at the end of each line
    octagon.dot()
    #Turns the turtle in preparation for drawing the next line
    octagon.left(45)
