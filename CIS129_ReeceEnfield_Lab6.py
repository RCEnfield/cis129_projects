# CIS129_ReeceEnfield_Lab6.py
# Module 6 Lab-6
# Reece Enfield
# March 3, 2024
# This program calculates the number of packages of hot dogs
# and the number of packages of hot dog buns needed for a
# cookout with the minimum amount of leftovers.

# Obtain the total number of hot dogs needed at the cookout
def getTotalHotDogs():
    # Request number of attendees
    attendees = int(input("Enter the number of people attending the cookout: "))
    # Request number of hot dogs served to each attendee
    hotDogs = int(input("Enter the number of hot dogs each attendee will be served: "))
    
    totalHotDogs = attendees * hotDogs
    return totalHotDogs

# Calculate and display the number of packages needed for both hot dogs
# and buns as well as the number of leftovers there will be
def showResults(totalHotDogs):
    # Constants for the number of hot dogs and buns in a package
    DOGS = 10
    BUNS = 8

    # Initializing variables
    dogsLeft = 0
    bunsLeft = 0
    minDogs = 0
    minBuns = 0

    # Calculate leftovers and minimum packages required
    dogsLeft = (DOGS - totalHotDogs % DOGS) % DOGS
    minDogs = (totalHotDogs // DOGS) + (0 ** (0 ** dogsLeft))
    bunsLeft = (BUNS - totalHotDogs % BUNS) % BUNS
    minBuns = (totalHotDogs // BUNS) + (0 ** (0 ** bunsLeft))
    
    # Display leftovers and minimum packages required
    print("Minimum packages of hot dogs needed:", minDogs)
    print("Minimum packages of hot dog buns needed:", minBuns)
    print("Hot dogs remaining:", dogsLeft)
    print("Hot dog buns remaining:", bunsLeft)

# Initialize totalHotDogs and call previous functions
totalHotDogs = getTotalHotDogs()
showResults(totalHotDogs)