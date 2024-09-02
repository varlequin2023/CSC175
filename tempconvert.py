#Temperature Converter by Vincent Arlequin - FA/24 CSC-175-02 - 09/06/24
#Input: Temperature in Fahrenheit (Whole Positive Number)
#Output: Temperature in Celsius and Kelvin
#To Do's: Obtain Fahrenheit temp in integer form, Convert the Fahrenheit temp to Celsius, Convert the Fahrenheit temp to Kelvin, Print the converted temps

#Obtain Fahrenheit temp from user, Force input to be integer, assign to var degF (since we're looking for a whole positive number)
degF = int(input("Enter a temperature (°F): "))

#Convert the Fahrenheit temp to Celsius using the formula provided, assign converted temp to var degC
degC = (degF - 32) * (5 / 9)

#Convert the Fahrenheit temp to Kelvin using the formula provided, assign converted temp to var kelvin
kelvin = (degF + 459.67)* (5 / 9)

#Display the converted temps to user
print(str(degF) + " °F is equal to " + str(degC) + " °C and " + str(kelvin) + " Kelvin.")
