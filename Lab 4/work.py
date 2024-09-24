# Assignment 4 by Vincent Arlequin - FA/24 CSC-175-02 - 09/27/24

# Importing Modules
import math
import random

# Part 2 - Round Up
# Takes number from user
numFloat = float(input("Enter a floating point number: "))

# Rounds given number up to the nearest integer
numInt = math.ceil(numFloat)

# Displays result to user
print("The number you gave rounds up to", numInt)

# Prints blank line to separate sections
print()


# Part 3 - Die Roll
# Takes die size from user
dieSize = int(input("Enter the number of sides you want the die to be: "))

# Generates a random number, equivalent to rolling an X sided die
dieRoll = random.randint(1, dieSize)

#Displays result to user
print("You rolled", dieRoll)

#Prints blank line to separate sections
print()


# Part 4 - Least Common Multiples
# Asks user for first number
lcm1 = int(input("Enter a number: "))

# Asks user for second number
lcm2 = int(input("Enter another number: "))

# Calculates the least common multiple of the given numbers
lcm = math.lcm(lcm1, lcm2)

# Displays result to user
print("The least common multiple of the numbers given is", lcm)

#Prints blank line to separate sections
print()


# Part 5 - Factorial Calculation
# Asks user for a number
factIn = int(input("Enter an integer: "))

# Initializes counter and factorial variables
count = 0
fact = 1

# Repeats calculation for factorial
for i in range(0, factIn):
    # Calculates factorial per equation
    fact = fact *(factIn - i)

# Displays result to user
print("The factorial of the number given is", fact)

#Prints blank line to separate sections
print()


# Part 6 - Liebniz's Formula
# Asks the user how many times the formula should be repeated
liebnizInt = int(input("How many iterations should be used to calculate pi? "))

# Initializes new pi variable
pi = 0

# Repeats calculation for pi
for i in range(liebnizInt):
    # Calculates pi using given formula
    pi = pi + ((4* ((-1)**i)) / (2*i+1))

# Displays result to user
print("When using the number of iterations given and Liebniz's formula to calculate pi, the result is", pi)


# Part 7 - When I run the file main.py, the program written within work.py runs.
