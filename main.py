# Lab 8 by Vincent Arlequin - FA/24 CSC-175-02 - 11/01/24

# Purpose: Returns the index of the first non-repeated character in a given string
# Assumptions: Parameter is a string
# Parameters: s, a string
# Post Conditions: Returns the index of the first non-repeated character in the string, if all are non-repeated returns 0, if all characters are repeated returns -1
def index_fnrc(s):
    # Initialize uniquecount variable
    uniquecount = 0

    # Counts the number of non-repeated/unique characters in the string
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            uniquecount = uniquecount + 1

    # If every character is non-repeated/unique, return 0
    if uniquecount == len(s):
        return 0

    # If no character is non-repeated/unique, return -1
    if uniquecount == 0:
        return -1

    # Finds the first non-repeated character and returns it
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i

# Purpose: Checks a given date and determines if it is valid
# Assumptions: Parameter is a string, date given follows mm/dd/yyyy format
# Parameters: date, a string
# Post Conditions: Returns True if the date is valid, False if the date is invalid 
def isvaliddate(date):
    # Separates the month, day, and year into individual strings
    month = date[0:2]
    day = date[3:5]
    year = date[6:10]

    # If there is a slash anywhere a number is expected - immediately returns false because the lengths of mm, dd, and yyyy are not valid
    if month.find("/") != -1 or day.find("/") != -1 or year.find("/") != -1:
        return False

    # Validates value lengths (mm must be 2, dd must be 2, yyyy must be 4)
    if len(month) == 2 and len(day) == 2 and len(year) == 4:

        # Validates month value (must be between 1 and 12)
        if int(month) > 0 and int(month) <= 12:

            # Validates day value (must be between 0 and 31)
            if int(day) > 0 and int(day) <= 31:

                # Validates year value (must be greater than 1999)
                if int(year) > 1999:

                    # If all tests are passed, date is valid, return True
                    return True

    # If a date fails any of these tests, date is invalid, return False
    return False
                
# Main Function - Takes user input and prints results of tests
def main():
    # Prompts user for a string
    string = input("Enter a string: ")
    # Calls index_fnrc() and prints the result with a message
    print("The index of the first non-repeating character in the string is", index_fnrc(string))

    # Prompts the user for a date in mm/dd/yyyy format
    user_date = input("Enter a date (must be in mm/dd/yyyy format): ")
    # Calls isvaliddate() and prints result with message
    print("Date is valid:", isvaliddate(user_date))

# Calls main function    
main()
