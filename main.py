# Challenge 3 by Vincent Arlequin - FA/24 CSC-175-02 - 12/13/24

# Purpose: Generates a cycle based on a list and a start value
# Assumptions: None
# Parameters: l - a list, start - an integer within the range len(l) - 1
# Post-Conditions: Returns a completed cycle OR "No Cycle" if cycle is impossible (based on start)
def cycleGen(l, start):
    # Start with a blank cycle list
    cycleList = []
    # Init complete, sets first index to start value
    complete = False
    index = start

    # While the cycle is not complete
    while complete == False:

        # Find the number at the index
        found = l[index]

        # Add the index to the cycle list
        cycleList.append(index)

        # Sets the index to the value found
        index = found

        # If whatever is found in the list is larger than len(l) - 1, return
        # "No Cycle" as it is impossible to complete a cycle
        if index > (len(l) - 1):
            return "No Cycle"

        # If the cycle has found the start value, the cycle is complete
        if found == start:
            complete = True

    # Returns the completed cycle
    return cycleList

# Purpose: Counts the number of complete & unique cycles within a given list
# Assumptions: cycleGen is properly defined and working
# Parameters: ls - a list
# Post-Conditions: Returns the number of complete & unique cycles
def cycleCount(ls):
    # Initalize allCycles, sortedCycles, and uniqueCycles
    allCycles = []
    sortedCycles = []
    uniqueCycles = []
    
    # Generates cycle for every possible start value, adds to the list of all cycles
    for i in range(len(ls)):
        cycle = cycleGen(ls, i)
        allCycles.append(cycle)

    # If one or more indexes within ls resulted in No Cycle, remove the result
    while "No Cycle" in allCycles:
        allCycles.remove("No Cycle")

    # Sorts Cycles for Easier Comparison
    for aCycle in allCycles:
        sortedCycles.append(sorted(aCycle))

    # For each sorted cycle, add to uniqueCycles if not already added
    for aCycle in sortedCycles:
        if aCycle not in uniqueCycles:
            uniqueCycles.append(aCycle)

    # Returns the total number of unique cycles for the given list
    return len(uniqueCycles)

def main():
    # Asks user for first number, init lst
    user = int(input("Enter an integer: "))
    lst = []

    # While the user hasn't input -1, append their input to lst and ask for more input
    while user != -1:
        lst.append(user)
        user = int(input("Enter an integer: "))

    # Calls cycleGen with lst as the list and 0 as start, prints result 
    print("Cycle with 0 as start:", cycleGen(lst, 0))

    # Calls cycleCount with lst as the list, prints result
    print("Number of unique cycles found within list:", cycleCount(lst))

main()
