# Lab 7 by Vincent Arlequin - FA/24 CSC-175-02 - 10/25/24

# Purpose: Prompts the user for a given amount of numbers, returns the average of the numbers entered
# Assumptions: Parameter is an integer greater than 0
# Parameters: Amount of numbers to be averaged
# Post Conditions: Returns the average of the numbers entered 
def iterativeAvg(iterations):
    # Initializes accumulator
    acc = 0
    # Repeats asking user for number & adding to total
    for i in range (iterations):
        # Prompts user for number
        number = float(input("Enter a number: "))
        # Adds number given to total
        acc = acc + number
    # Calculates and returns final average
    return acc / iterations

# Purpose: Calculates the nth number of the Fibonacci Sequence using a for loop
# Assumptions: Parameter is an integer greater than 0
# Parameters: The number in the Fibonacci Sequence that the user wishes to calculate
# Post Conditions: Returns the number in the Fibonacci Sequence that the user wishes to calculate
def forFibonacci(n):
    # Initializes the beginning of the Fibonacci Sequence
    prev2 = 1
    prev1 = 0
    # Repeats the calculation to find the requested number using the formula
    for i in range(n):
        fibonacciNumber = prev2 + prev1
        prev2 = prev1
        prev1 = fibonacciNumber
    # Returns the final calculated number of the Fibonacci Sequence
    return fibonacciNumber

# Purpose: Calculates the nth number of the Fibonacci Sequence using a while loop
# Assumptions: Parameter is an integer greater than 0
# Parameters: The number in the Fibonacci Sequence that the user wishes to calculate
# Post Conditions: Returns the number in the Fibonacci Sequence that the user wishes to calculate
def whileFibonacci(n):
    # Initializes the beginning of the Fibonacci Sequence and the counter for the while loop
    prev2 = 1
    prev1 = 0
    counter = 0
    # Repeats the calculation to find the requested number using the formula
    while counter != n:
        fibonacciNumber = prev2 + prev1
        prev2 = prev1
        prev1 = fibonacciNumber
        # Increments the counter for every time the number is calculated
        counter = counter + 1
    # Once the formula is run n times, the result is returned.
    return fibonacciNumber

def main():
    # Initializes valid variable
    valid = False
    # While the result is invalid (or doesn't exist), keep prompting the user for a new one
    while valid == False:
        # Asks the user for the number of numbers they wish to average
        n = int(input("Enter the number of numbers you wish to average: "))
        # Checks if the input is valid (greater than or equal to 1)
        if n >= 1:
            # If valid, calls the function to average the numbers and prints the result
            print("The average of the numbers entered is", iterativeAvg(n))
            # Stops the while loop
            valid = True
        # If input is invalid, prints error and prompts user for a new number
        else:
            print("The number you entered is invalid. Please enter a valid number.")
    # Asks the user to input the number of the Fibonacci sequence that they would like to calculate
    nFibonacci = int(input("Enter the number of the Fibonacci sequence that you would like to calculate: "))
    # Calls the forFibonacci() function, calculates number using for loop, prints result
    print("The number you requested (calculated with a for loop) is", forFibonacci(nFibonacci))
    # Calls the whileFibonacci() function, calculates number using while loop, prints result
    print("The number you requested (calculated with a while loop) is", whileFibonacci(nFibonacci))

# Calls main function 
main()

# TEST CASE 1 - BLACK BOX
# For Part 1 (Average), user enters 5, then 6, -7, 32, 54.2, -33.2 - recieves 10.4 as the average.
# For Part 2 (Fibonacci), user enters 7 - recieves 13 for both the for loop and the while loop results.
# WHITE BOX
# The while loop in the main() function first asks the user for a number. The user enters 5. The if statement
# in the while loop determines the input to be valid, and calls the iterativeAvg() function. This function asks
# the user for 5 numbers and adds each number together. Once done, it divides the sum of the numbers entered
# by the number of numbers entered, and returns it to the function call, which prints the resulting average (10.4).
# The main() function then asks the user for the number in the Fibonacci Sequence that they would like to calculate.
# The user enters 7. The forFibonacci() and whileFibonacci() functions are called (these functions operate similarly,
# I will note where differences are), which first initializes the prev2 and prev1 variables (the "while" function also
# initializes a counter variable which will be used in the while loop). The calculation then uses the formula given
# to calculate the first number of the sequence, then it stores the previous numbers in the variables prev2 and prev1, 
# so that the previous two numbers are stored so that the next number can be calculated. This calculation then repeats
# until the desired number is calculated (in the "for" function this is done using a for loop repeating the number of times
# the user specifies, in the "while" function this is done by using a counter variable, incrementing by 1 every time the 
# equation is done, and the while loop terminating once the counter is equal to the number given). In the end, the results are
# returned to the function calls and the results are printed on screen for the user to read (13).
#
# TEST CASE 2 - BLACK BOX
# For Part 1 (Average), user enters 6, then 5, -4, 3, 22.1, -25.5, 1353 - recieves 225.6 as the average.
# For Part 2 (Fibonacci), user enters 2 - recieves 1 for both the for loop and the while loop results.
# WHITE BOX
# The while loop in the main() function first asks the user for a number. The user enters 6. The if statement
# in the while loop determines the input to be valid, and calls the iterativeAvg() function. This function asks
# the user for 6 numbers and adds each number together. Once done, it divides the sum of the numbers entered
# by the number of numbers entered, and returns it to the function call, which prints the resulting average (225.6).
# The main() function then asks the user for the number in the Fibonacci Sequence that they would like to calculate.
# The user enters 2. The forFibonacci() and whileFibonacci() functions are called (these functions operate similarly,
# I will note where differences are), which first initializes the prev2 and prev1 variables (the "while" function also
# initializes a counter variable which will be used in the while loop). The calculation then uses the formula given
# to calculate the first number of the sequence, then it stores the previous numbers in the variables prev2 and prev1, 
# so that the previous two numbers are stored so that the next number can be calculated. This calculation then repeats
# until the desired number is calculated (in the "for" function this is done using a for loop repeating the number of times
# the user specifies, in the "while" function this is done by using a counter variable, incrementing by 1 every time the 
# equation is done, and the while loop terminating once the counter is equal to the number given). In the end, the results are
# returned to the function calls and the results are printed on screen for the user to read (1).
#
# TEST CASE 3 - BLACK BOX
# For Part 1 (Average), user enters -1, user recieves error and prompt for new number - user enters 3 and 
# then 6, 0, 4 - recieves 3.3333333333333335 as the average.
# For Part 2 (Fibonacci), user enters 11 - recieves 89 for both the for loop and the while loop results.
# WHITE BOX
# The while loop in the main() function first asks the user for a number. The user enters -1. The if statement
# in the while loop determines the input to be invalid, which then prints an error message, and a prompt for
# a new number. The user enters 3. The if statement in the while loop determines the input to be valid, and calls 
# the iterativeAvg() function. This function asks the user for x numbers and adds each number together. Once done, 
# it divides the sum of the numbers entered by the number of numbers entered, and returns it to the function call,
# which prints the resulting average (3.3333333333333335).
# The main() function then asks the user for the number in the Fibonacci Sequence that they would like to calculate.
# The user enters 11. The forFibonacci() and whileFibonacci() functions are called (these functions operate similarly,
# I will note where differences are), which first initializes the prev2 and prev1 variables (the "while" function also
# initializes a counter variable which will be used in the while loop). The calculation then uses the formula given
# to calculate the first number of the sequence, then it stores the previous numbers in the variables prev2 and prev1, 
# so that the previous two numbers are stored so that the next number can be calculated. This calculation then repeats
# until the desired number is calculated (in the "for" function this is done using a for loop repeating the number of times
# the user specifies, in the "while" function this is done by using a counter variable, incrementing by 1 every time the 
# equation is done, and the while loop terminating once the counter is equal to the number given). In the end, the results are
# returned to the function calls and the results are printed on screen for the user to read (89).
