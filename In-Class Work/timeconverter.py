#Time Converter by Vincent Arlequin - FA/24 CSC-175-02 - 09/02/24
#Problem: Convert 24 hr time to 12 hr time (only hours, ignores AM/PM)
#Test Data:
#in: 13 out: 1
#in 16 out:4
#in 5 out: 5
hours24 = int(input("Enter an hour: "))
hours12 = hours24 % 12
print(hours12)
