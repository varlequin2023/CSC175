#Division by Vincent Arlequin - FA/24 CSC-175-02 - 09/06/24
#Input: A and B (Both Positive, Whole Numbers - i.e. integers)
#Output: Quotient & Remainder for both A/B and B/A
#To Do's: Obtain A & B as integers, Calculate quotient and remainder for A/B, Calculate quotient and remainder for B/A, Display results to user

#Obtain value A from user, force it to be an integer (since we're working with a positive, whole number), and assign it to var valueA
valueA = int(input("Enter a value (A) (positive whole number only): "))

#Obtain value B from user, force it to be an integer (since we're working with a positive, whole number), and assign it to var valueB
valueB = int(input("Enter another value (B) (positive whole number only): "))


#Calculate the quotient for A/B, assign it to var quotientAB
quotientAB = valueA // valueB

#Calculate the remainder for A/B, assign it to var remainderAB
remainderAB = valueA % valueB

#Display the results of A/B, converting the values to strings so we can concatenate into one sentence 
print("When dividing " + str(valueA) + " (A) by " + str(valueB) + " (B) the quotient will be " + str(quotientAB) + " and the remainder will be " + str(remainderAB) + ".") 


#Calculate the quotient for B/A, assign it to var quotientBA
quotientBA = valueB // valueA

#Calculate the remainder for B/A, assign it to var remainderBA
remainderBA = valueB % valueA

#Display the results of B/A, converting the values to strings so we can concatenate into one sentence 
print("When dividing " + str(valueB) + " (B) by " + str(valueA) + " (A) the quotient will be " + str(quotientBA) + " and the remainder will be " + str(remainderBA) + ".")
