# Lab 5 by Vincent Arlequin - FA/24 CSC-175-02 - 10/04/24

# Purpose: Checks if a given number is divisible by 4 but not by 20
# Assumptions: Parameter given is an integer
# Parameters: An integer
# Post Conditions: Returns the result of the test
def divisibleCheck(n):
    # Determines if the given number is divisible by 4 and not by 20
    if (n % 4 == 0) and (n % 20 != 0):
        # If the number meets the criteria given, returns True
        return True
    # If the given number does not meet the criteria, returns False
    else :
        return False

# Purpose: Checks if a given number is either even or less than 100 (but not both)
# Assumptions: Parameter given is an integer
# Parameters: An integer
# Post Conditions: Returns the result of the test
def evenOrLessThan100(n):
    # Determines if the given number is either even or less than 100 (but not both)
    if ((n % 2 == 0) and n >= 100) or ((n % 2 != 0) and (n < 100)):
        # If the given number meets the criteria given, returns True
        return True
    # If the given number does not meet the criteria, returns False
    else:
        return False

# Purpose: Checks if a given number is between 100 and 200, inclusively
# Assumptions: Parameter given is an integer
# Parameters: An integer
# Post Conditions: Returns the result of the test
def between100and200(n):
    # Determines if the given number is between 100 and 200, inclusively
    if(n >= 100) and (n <=200):
        # If the given number is within the range, returns True
        return True
    # If the given number is not within the range, returns False
    else:
        return False

# Purpose: Checks if a given year is a leap year (and that the number is greater than 0)
# Assumptions: Parameter given is an integer, greater than 0
# Parameters: An integer, greater than 0
# Post Conditions: Returns if the year given is a leap year or not, or if the year given is invalid
def leapYearCheck(y):
    # Determines if year is greater than 0, and if it is less than 1582
    if (y > 0) and (y < 1582):
        # Determines if year is divisible by 4 (criteria for determining leap years before 1582)
        if (y % 4 == 0):
            # If year meets criteria, returns True
            return True
        # If year does not meet crieteria, returns False
        else:
            return False
    # Determines if year is greater than or equal to 1582
    elif (y >= 1582):
        # Determines if year is divisible by 400 or if it is divisible by 4 but not 400 (criteria for determining leap years from 1582 onwards)
        if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
            # If year meets criteria, returns True
            return True
        #If year does not meet criteria, returns False
        else:
            return False
    # If year is less than or equal to 0
    else:
        # Returns that the year given is invalid because it is less than or equal to 0
        return "Entry Invalid"

# main() function that runs all other functions as needed
def main():
    # Asks user for a number to use with first 3 functions
    num = int(input("Enter a Number: "))
    # Checks if number given is divisible by 4, but not 20
    print("Number is divisible by 4, but not 20:", divisibleCheck(num))
    # Checks if number given is even or less than 100, but not both
    print("Number is even or less than 100, but not both:", evenOrLessThan100(num))
    # Checks if number given is between 100 and 200, inclusively
    print("Number is between 100 and 200, inclusively:", between100and200(num))

    # Asks user for a year
    year = int(input("Enter a year: "))
    # Checks to see if given year is a leap year, or if the given year is invalid
    print("Year given is leap year:", leapYearCheck(year))

# Runs main() function
main()
