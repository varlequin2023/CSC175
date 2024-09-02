#Circle Calculator by Vincent Arlequin - FA/24 CSC-175-02 - 09/06/24
#Input: Radius of a Circle (Whole Positive Number)
#Output: Circumference and Area of the Circle
#To Do's: Obtain radius of the circle in integer form, Calculate the area of the circle, Calculate the circumference of the circle, Print area and circumference

#Import math functions (i.e. pi)
import math

#Obtain radius of circle, force it to be an integer (since we are only looking for a whole positive number), store in var radius
radius = int(input("Enter the radius of the circle: "))

#Calculate circumference using equation, store in var circumference
circumference = 2 * math.pi * radius

#Calculate area using equation, store in var area
area = math.pi * (radius ** 2)

#Display calculated area and circumference to user, converts the integers to strings in order to concatenate with the rest of the sentence
print("A circle with a radius of " + str(radius) + " has a circumference of "+ str(circumference) + " and an area of " + str(area) + ".")
