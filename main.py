# Lab 11 by Vincent Arlequin - FA/24 CSC-175-02 - 11/22/24

# Purpose: Checks if a number is greater than 0 recursively
# Assumptions: user_input is an integer
# Parameters: user_input, an integer
# Post Conditions: Returns either "input is valid" if input > 0, or asks for a new number and checks it again if not, until a number > 0 is entered.
def input_validation(user_input):
    # If user input is greater than 0, returns "Input is valid"
    if user_input > 0:
        return "Input is valid"
    # if user input is not valid, prompts the user for a new entry and runs it through the input_validation() function again
    else:
        return input_validation(int(input("Input is invalid, please enter a new number: "))) 

# Purpose: Computes an alternating sum on the items in the given list
# Assumptions: alist is a list, add_sub is either True or False
# Parameters: alist - a list, add_sub is False if next operation is -, True if next operation is +, start - an integer that indicates where the function starts the calculation
# Post Conditions: Returns the alternating sum of the items in the list
def alt_sum(alist, add_sub, start):
    # Base case, if start is equal to the length of the list, returns 0
    if start == len(alist):
        return 0
    else:
        # Logic to determine if + or - is the next operator, as well as doing the math for the alternating sum
        if add_sub == True:
            return alist[start] + alt_sum(alist, False, start + 1)
        elif add_sub == False:
            return (-1 * alist[start]) + alt_sum(alist, True, start + 1)
        
# Purpose: Pushes a given list through alt_sum() with default settings
# Assumptions: list parameter is a list, alt_sum() is properly defined
# Parameters: list, a list
# Post Conditions: Returns the result of alt_sum() with the given list, add_sub = True, start = 0
def inputList_altsum(list):
    return alt_sum(list, True, 0)

# Main Function
def main():
    # Asks for number from user, and runs it through input_validation, eventually printing the final result
    num = int(input("Enter a number: "))
    print(input_validation(num))

    # Asks for a space delinated list from the user, converts it into a list, and converts each item in the list to an integer
    user_list = input("Enter a list of numbers, each number separated by a space: ")
    user_list = user_list.split()
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
    # Prints the result of alt_sum() with this list and default settings as set in inputList_altsum()
    print("When this list is run through alt_sum with default settings, the result is", inputList_altsum(user_list))

# Calls main function
main()

# TEST CASES - input_validation()
# -3 -> Input is invalid, prompt for a new number
# -1 -> Input is invalid, prompt for a new number
# 0 -> Input is invalid, prompt for a new number
# 1 -> Input is valid
# 2 -> Input is valid
# 423 -> Input is valid
# 75 -> Input is valid
# 88 -> Input is valid
# 45 -> Input is valid

# TEST CASES - alt_sum()
# 3 4 1 -> 0
# 7 42 91 -> 56
# 32 69 42 11 -> -6
# 19 -12 34 -> 65
# 12 4 -> 8
# 17 45 54 -> 26
