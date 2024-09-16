#Lab 2 - Vincent Arlequin - FA/24 CSC-175-02 - 09/13/24

#Problem 1 - Corrected Code:
#name = input('What is your name? ')
#print("Your name is", name)
#1b. The Python interpreter will detect an error in the print statement on line 2 as there is a capital P in the print statement when it should be lowercase.
#1c. The Python interpreter will display a name error because it thinks "Print" is an undefined variable.

#Problem 2 - Corrected Code:
#name = input('What is your age? ')
#print("Your age is", name)
#2b. The Python interpreter will detect an error in the print statement on line 2 as the string "Your name is" is never closed with quote marks.
#2c. The Python interpreter will display a syntax error, noting that there is an unterminated string.

#Problem 3 - Corrected Code:
#age = int(input('What is your age? '))
#print("In a decade you will be", age+10 , "years old.")
#print("In a score you will be", age+20, "years old.")
#3b. The Python interpreter will first detect an error in the print statement on line 2, stating that you can only concatenate strings with other strings (age+10).
#3c. The Python interpreter will display a Type error because it thinks you want to combine the contents of variable age with 10 (instead of adding 10 to the value of age), because age is originally a string and not an integer.
#3d. The second error in this program is in line 3. The "age+20" is encapulated within the quotation marks, which Python reads as part of the string and not a separate variable.
#3e. The second error wasn't detected by Python because it's a logic error, the program isn't broken when Python is concerned, but it isn't doing what we want it to do.

#Problem 7:
#Multi Shape Draw by Vincent Arlequin - FA/24 CSC-175-02 - 09/13/24
#To Do's: Draw a circle w/ green fill, a octagon w/ dots at vertexes, and a pentagon w/ red fill

#Importing Turtle library
import turtle

#Initializing Turtle
t = turtle.Turtle()

#DRAW CIRCLE

#Moves turtle to circle start point
t.penup()
t.goto(0,-100)
t.pendown()

#Set line and fill color to green for circle
t.pencolor("green")
t.fillcolor("green")

#Begins fill (so that the circle can be filled with green)
t.begin_fill()

#Draws Circle
t.circle(200)

#Completes and fills circle
t.end_fill()

#DRAW OCTAGON

#Moves turtle to octagon start point
t.penup()
t.goto(0,0)
t.pendown()

#Set line color to black for octagon
t.pencolor("black")

#Loop that repeats drawing the necessary lines for drawing the octagon
for i in range(8):
    #Draws a 50 unit line
    t.forward(100)
    #Adds a dot at the end of each line
    t.dot()
    #Turns the turtle in preparation for drawing the next line
    t.left(45)

#DRAW PENTAGON

#Moves turtle to pentagon start point
t.penup()
t.goto(0,100)
t.pendown()

#Set line and fill colors to red for pentagon
t.pencolor("red")
t.fillcolor("red")

#Begins fill (so that the pentagon can be filled with red)
t.begin_fill()

#Loop that repeats drawing the necessary lines for a drawing the pentagon
for i in range(5):
    #Draws a 50 unit line
    t.forward(50)
    #Turns the turtle in preparation for drawing the next line
    t.left(72)

#Completes and fills pentagon
t.end_fill()
