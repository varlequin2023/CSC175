# Lab 12 by Vincent Arlequin - FA/24 CSC-175-02 - 12/6/24

class Flight:

    # Purpose: Initializes Flight object
    # Assumptions: Departure, Destination, and Distance are provided
    # Parameters: Self, Departure, Destination, and Distance
    # Post Conditions: Created Flight object with the specified parameters
    def __init__(self, departure, destination, distance):
        self.mydeparture = departure
        self.mydestination = destination
        self.mydistance = distance

    # Purpose: Gets and returns the departure point of a given Flight Object
    # Assumptions: Flight object is created and has a departure point
    # Parameters: self
    # Post Conditions: Returns the departure point of a given Flight Object 
    def getMyDeparture(self):
        return self.mydeparture

    # Purpose: Gets and returns the destination of a given Flight Object
    # Assumptions: Flight object is created and has a destination
    # Parameters: self
    # Post Conditions: Returns the destination of a given Flight Object
    def getMyDestination(self):
        return self.mydestination

    # Purpose: Gets and returns the distance value of a given Flight Object
    # Assumptions: Flight object is created and has a distance value
    # Parameters: self
    # Post Conditions: Returns the distance value of a given Flight Object
    def getMyDistance(self):
        return self.mydistance

    # Purpose: Calculates travel time from departure to destination
    # Assumptions: Flight object is created and has a distance value (in miles), 
    # Parameters: self, speed (in miles per hour)
    # Post Conditions: returns travel time (in X hour(s) Y minute(s) format)
    def traveltime(self, speed):
        # Calculates travel time, converts to minutes
        traveltime = int((self.mydistance/speed) * 60)
        # Calculates number of hours and minutes, rounds to nearest minute (down, so 59.87 is 59)
        travelhours = int(traveltime // 60)
        travelminutes = int(traveltime % 60)
        # Returns number of hours and minutes needed to travel distance given (in X hour(s) Y minute(s) format)
        return str(travelhours) + " hour(s) " + str(travelminutes) + " minute(s)"

    # Purpose: Computes a complete flight object from two separate flight objects (from A -> B, B-> C to A -> C)
    # Assumptions: self has all required values, flight2 is a flight object and has required values
    # Parameters: self and flight2, Flight objects
    # Post Conditions: If valid flight pair, returns a flight object with combined values, returns "None" if invalid
    def extend(self, flight2):
        # If the destination of self does not match the departure of flight2, return "None"
        if self.mydestination != flight2.mydeparture:
            return "None"
        # If flight pairing is valid, return a new flight object with the departure point of self, destination of flight2, and the combined distance of both flights 
        else:
            return Flight(self.mydeparture, flight2.mydestination, self.mydistance + flight2.mydistance)

    # Purpose: Formats layout of a printed Flight object
    # Assumptions: self has all required values
    # Parameters: self
    # Post Conditions: Returns a formatted string with all three values of the Flight object
    def __str__(self):
        return ("Flight from " + str(self.mydeparture) + " to " + str(self.mydestination) + " - Distance: " + str(self.mydistance) + " miles")

# Main Function  
def main():
    # Asks user for first flight's information, creates Flight object
    flt1_departure = input("Please enter the departure point for Flight 1: ")
    flt1_destination = input("Please enter the destination for Flight 1: ")
    flt1_distance = int(input("Please enter the distance between these points (in miles): "))
    flight1 = Flight(flt1_departure, flt1_destination, flt1_distance)
    print("--")

    # Asks user for second flight's information, creates Flight object
    flt2_departure = input("Please enter the departure point for Flight 2: ")
    flt2_destination = input("Please enter the destination for Flight 2: ")
    flt2_distance = int(input("Please enter the distance between these points (in miles): "))
    flight2 = Flight(flt2_departure, flt2_destination, flt2_distance)
    print("--")

    # Generates combination of Flights 1 and 2
    combinedFlight = flight1.extend(flight2)

    # Tests getter & traveltime methods with Flight 1
    print("Flight 1 Departure Point:", flight1.getMyDeparture())
    print("Flight 1 Destination:", flight1.getMyDestination())
    print("Flight 1 Distance:", flight1.getMyDistance(), "miles")
    print("--")
    
    # Tests getter & traveltime methods with Flight 2
    print("Flight 2 Departure Point:", flight2.getMyDeparture())
    print("Flight 2 Destination:", flight2.getMyDestination())
    print("Flight 2 Distance:", flight2.getMyDistance(), "miles")
    print("--")

    # Asks for speed (in MPH) from user, calculates and prints the travel times for both Flight 1 and 2
    speed = int(input("Enter the speed at which these flights will travel (in miles per hour): "))
    print("Length of Flight 1 (rounded to the lowest minute):", flight1.traveltime(speed))
    print("Length of Flight 2 (rounded to the lowest minute):", flight2.traveltime(speed))
    print("--")

    # If Flights 1 & 2 can not be combined, print error message
    if combinedFlight == "None":
        print("A combination of Flights 1 & 2 could not be computed.")
    # Prints information for combined flight if combination can be computed
    else:
        print("Combined Flight Departure Point:", combinedFlight.getMyDeparture())
        print("Combined Flight Destination:", combinedFlight.getMyDestination())
        print("Combined Flight Distance:", combinedFlight.getMyDistance(), "miles")
        print("Length of Combined Flight (rounded to the lowest minute):", combinedFlight.traveltime(speed))

# Calls main function        
main() 

# -------- TEST CASES --------
# Test Case 1 - Data Entered
# Departure Point for Flight 1: Binghamton
# Destination for Flight 1: Detroit
# Distance for Flight 1 (in miles): 365
# --
# Departure Point for Flight 2: Detroit
# Destination for Flight 2: Las Vegas
# Distance for Flight 2 (in miles): 1758
# --
# Speed (in miles per hour):
# --
# Test Case 1 - Expected Results
# Flight 1 Departure Point: Binghamton
# Flight 1 Destination: Detroit
# Flight 1 Distance: 365 miles
# --
# Flight 2 Departure Point: Detroit
# Flight 2 Destination: Las Vegas
# Flight 2 Distance: 1758 miles
# --
# Length of Flight 1: 0 hour(s) 40 minute(s)
# Length of Flight 2: 3 hour(s) 12 minute(s)
# --
# Combined Departure Point: Binghamton
# Combined Flight Destination: Las Vegas
# Combined Flight Distance: 2123 miles
# Combined Flight Length: 3 hour(s) 52 minute(s)
#
# Test Case 2 - Data Entered
# Departure Point for Flight 1: New York
# Destination for Flight 1: London
# Distance for Flight 1 (in miles): 3456
# --
# Departure Point for Flight 2: London
# Destination for Flight 2: Moscow
# Distance for Flight 2 (in miles): 1553
# --
# Speed (in miles per hour): 575
# --
# Test Case 2 - Expected Results
# Flight 1 Departure Point: New York
# Flight 1 Destination: London
# Flight 1 Distance: 3456 miles
# --
# Flight 2 Departure Point: London
# Flight 2 Destination: Moscow
# Flight 2 Distance: 1553 miles
# --
# Length of Flight 1: 6 hour(s) 0 minute(s)
# Length of Flight 2: 2 hour(s) 42 minute(s)
# --
# Combined Departure Point: New York
# Combined Flight Destination: Moscow
# Combined Flight Distance: 5009 miles
# Combined Flight Length: 8 hour(s) 42 minute(s)
#
# Test Case 3 - Data Entered
# Departure Point for Flight 1: Albany
# Destination for Flight 1: Boston
# Distance for Flight 1 (in miles): 139
# --
# Departure Point for Flight 2: Syracuse
# Destination for Flight 2: Boston
# Distance for Flight 2 (in miles): 262
# --
# Speed (in miles per hour): 561
# --
# Test Case 3 - Expected Results
# Flight 1 Departure Point: Albany
# Flight 1 Destination: Boston
# Flight 1 Distance: 139 miles
# --
# Flight 2 Departure Point: Syracuse
# Flight 2 Destination: Boston
# Flight 2 Distance: 262 miles
# --
# Length of Flight 1: 0 hour(s) 14 minute(s)
# Length of Flight 2: 0 hour(s) 28 minute(s)
# --
# Combined Flight Can Not Be Computed
