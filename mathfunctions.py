#Math Functions by Vincent Arlequin - FA/24 CSC-175-02 - 09/20/24
#To Do: Calculate Circumference from Radius, Calculate Volume from L, W, H, Convert Fahrenheit temp to Celsius, Calculate x-value from m & b

#Imports Math Module
import math

#Purpose: Given the Radius of a Circle, calculate the Circumference of the Circle
#Assumptions: Given Radius Parameter is a number (i.e. int)
#Inputs: Radius
#Post Conditions: Returns the Circumference of the Circle
def circumference(rad):
    return 2 * math.pi * rad

#Purpose: Given the Length, Width, and Height of a box, calculate the volume of the box 
#Assumptions: Length, Width, and Height are numbers (i.e. int)
#Inputs: Length, Width, and Height
#Post Conditions: Returns the volume of the box
def volumecalc(length, width, height):
    return length * width * height

#Purpose: Convert a given temperature in Fahrenheit to Celsius
#Assumptions: The given temperature is in Fahrenheit and is a number (i.e. int)
#Inputs: Temperature in Fahrenheit
#Post Conditions: Returns the converted temperature in Celsius
def tempconvert(degF):
    return (degF - 32) * (5 / 9)

#Purpose: Given the values of coefficients m & b, calculate at what x-value will the function cross the x-axis
#Assumptions: The given m & b values are numbers (i.e. integers)
#Inputs: m & b values
#Post Conditions: Returns the x-value at which the function will cross the x-axis
def xcalc(m, b):
    return -b / m

#Main Function that Gathers User Input, Calls Functions, and Prints Results
def main():

    #Gathers radius from user, calculates circumference using circumference() function, prints circumference and an extra line (to separate different functions)
    r = int(input("Enter a circle's radius: "))
    print("A circle with the given radius would have a circumference of", circumference(r))
    print()

    #Gathers length, width, and height from user, calculates volume using volumecalc() function, prints volume and an extra line (to separate different functions)
    l = int(input("Enter the length of a box: "))
    w = int(input("Enter the width of a box: "))
    h = int(input("Enter the height of a box: "))
    print("The volume of a box with the given measurements would be", volumecalc(l, w, h))
    print()

    #Gathers temp in degrees F from user, converts to C using tempconvert() function, prints converted temperature and an extra line (to separate different functions)    
    temp = int(input("Enter a temperature in Fahrenheit: "))
    print("The given Fahrenheit temperature would be equal to", tempconvert(temp), "in Celsius")
    print()

    #Gathers m & b values from user, calculates x-intercept using xcalc() function, prints x-intercept and an extra line (to separate different functions)
    coefficientM = int(input("Enter the value of coefficient m: "))
    coefficientB = int(input("Enter the value of coefficient b: "))
    print("Based on the given m and b values, the function will cross the x-axis at x-value", xcalc(coefficientM, coefficientB))

#Runs main() function as defined above
main()
    
