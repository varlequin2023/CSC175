# Lab 9 by Vincent Arlequin - FA/24 CSC-175-02 - 11/08/24

# Purpose: Given 2 lists (a & b), determine the index at which b is contained within a
# Assumptions: Parameters are lists
# Parameters: a & b, both lists
# Post Conditions: Returns the index at which b is contained within a
def contains(a, b):
    # Repeats check for the entirety of list a's length
    for i in range(len(a)):
        # Checks to see if a given part of list a is the same as list b
        if a[i : i + len(b)] == b:
            # Once the part checked matches list b, returns the index at which this occurs
            return i
    # If list b is found nowhere in list a, returns "Not Found"
    return "Not Found"

# Purpose: Given 2 lists (a & b), determine the index at which b is contained within a, skipping allowed
# Assumptions: Parameters are lists
# Parameters: a & b, both lists
# Post Conditions: Returns the index at which b is contained within a
def enmeshes(a, b):
    # Initializes Variables
    index = 0
    prevIndex = 0
    found = 0
    # Repeats check for every item in list b
    for i in range(len(b)):
        # If an element in b is not in a, return "Not Found"
        if a.count(b[i]) == 0:
            return "Not Found"
        # Finds the index in a of the item in b
        index = a.index(b[i])
        # If this item is after the previous item, increment found by 1
        if index >= prevIndex:
            found = found + 1
            prevIndex = index
    # If every item in b was found in a, and in the correct order, retun the index of b[0] in a (i.e. the first occurance of b in a)
    if found == len(b):
        return a.index(b[0])
    # If b is not contained in a, return "Not Found"
    return "Not Found"
        
# Main Function
def main():
    # Accepts list a from user, splits into list
    list_a = input("Enter list a (each value must be separated by a space): ")
    list_a = list_a.split()
    # Accepts list b from user, splits into list
    list_b = input("Enter list b (each value must be separated by a space): ")
    list_b = list_b.split()
    # Calls contains(), prints and returns result
    print("The index at which list a contains list b is:", contains(list_a, list_b))
    # Calls enmeshes(), prints and returns result
    print("The index at which list a contains list b (skipping allowed) is:", enmeshes(list_a, list_b))

# Calls Main Function
main()

# TEST CASES
# #     List A      List B      contains() result       enmeshes() result
# 1.    3 1 4 7 6   2 3         Not Found               Not Found
# 2.    3 2 4 1 5   2 4 1       1                       1
# 3.    7 2 1 3 6   2 1 3       1                       1
# 4.    7 8 1 2 3   2 3         3                       3
# 5.    5 6 1 2 3   4 8         Not Found               Not Found
# 6.    6 4 5 7     6 5         Not Found               0 
# 7.    7 3 4 5 6   7 4 6       Not Found               0
# 8.    7 3 4 5 6   3 5 6       Not Found               1
# 9.    7 3 1 2 4   7 1 4 3     Not Found               Not Found 
# 10.   7 6 5 4 3   2 1         Not Found               Not Found 
