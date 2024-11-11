# Lab 10 by Vincent Arlequin - FA/24 CSC-175-02 - 11/15/24

# Purpose: Counts and returns the number of characters in a given file object
# Assumptions: "file" parameter is a file object
# Parameters: file, a file object
# Post Conditions: Returns the number of characters in the file object
def charCount(file):
    # Moves file pointer to the beginning of the file
    file.seek(0)
    # Puts the information in the file into a string 
    fileContent = file.read()
    # Returns the length of the file content (i.e. the number of characters in the file)
    return len(fileContent)

# Purpose: Counts and returns the number of lines in a given file object
# Assumptions:"file" parameter is a file object
# Parameters: file, a file object 
# Post Conditions: Returns the number of lines in the file object
def lineCount(file):
    # Initialize counter and move file pointer to the beginning of the file
    count = 0
    file.seek(0)
    # Counts each line in the file
    for aline in file:
        count = count + 1
    # Returns the number of lines in the file
    return count

# Purpose: Counts and returns the number of lowercase letters in a given file object
# Assumptions:"file" parameter is a file object
# Parameters: file, a file object
# Post Conditions: Returns the number of lowercase letters in the file object
def lowerCount(file):
    # Initialize counter and move file pointer to the beginning of the file
    count = 0
    file.seek(0)
    # For each line in the file
    for line in file:
        # For each character in the line
        for i in range(len(line)):
            # If the character is lowercase, count it
            if line[i].islower():
                count = count + 1
    # Returns the number of lowercase letters counted
    return count

# Purpose: Counts and returns the number of uppercase letters in a given file object
# Assumptions:"file" parameter is a file object
# Parameters: file, a file object
# Post Conditions: Returns the number of uppercase letters in the file object
def upperCount(file):
    # Initialize counter and move file pointer to the beginning of the file
    count = 0
    file.seek(0)
    # For each line in the file
    for line in file:
        # For each character in the line
        for i in range(len(line)):
            # If the character is uppercase, count it
            if line[i].isupper():
                count = count + 1
    # Returns the number of uppercase letters counted
    return count

# Purpose: Counts the total number of each letter in a given file object
# Assumptions:"file" parameter is a file object
# Parameters: file, a file object
# Post Conditions: Returns a dictionary with the letter as the key and the number of occurances as the value
def letterOccurCounter(file):
    # Initialize dictionary and move file pointer to the beginning of the file
    file.seek(0)
    dict = {}
    # Puts the information in the file into a string
    fileContent = file.read()
    # For each character in the file, which is made lowercase
    for char in fileContent.lower():
        # If the character is a letter
        if char.isalpha():
            # If the character is already in the dictionary, add 1 to the count
            if char in dict:
                dict[char] = dict[char] + 1
            # If the character is not in the dictionary, add it to the dictionary and count it
            else:
                dict[char] = 1
    # Returns the dictionary with the count of the letters
    return dict
           
# Main Function
def main():
    # Opens MA_01.txt as a file object, store it in myFile
    myFile = open('MA_01.txt')
    # Calls charCount() and prints the total number of characters in the file
    print("Total # of Characters:", charCount(myFile))
    # Calls lineCount() and prints the total number of lines in the file
    print("Total # of Lines:", lineCount(myFile))
    # Calls lowerCount() and prints the total number of lowercase letters in the file
    print("Total # of Lowercase Letters:", lowerCount(myFile))
    # Calls upperCount() and prints the total number of uppercase letters in the file
    print("Total # of Uppercase Letters:", upperCount(myFile))

    # Prints blank line
    print("")
    # Calls letterOccurCounter() and stores the resulting directory in letterOccurances
    letterOccurances = letterOccurCounter(myFile)
    # Prints the key for the rest of the data
    print("Letter - Count")
    # Prints the dictionary, each letter and count on a separate line
    for key in letterOccurances:
        print(key,"-",letterOccurances[key])
    # Closes the file    
    myFile.close()

# Calls main function  
main()
