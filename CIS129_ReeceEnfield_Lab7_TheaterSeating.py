# CIS_129_ReeceEnfield_Lab7_TheaterSeating.py
# Reece Enfield
# March 11, 2024
# This program displays the income generated from ticket sales at a dramatic theater

# Initialize program loop condition
runAgain = 'yes'

# Main function
def main():
    # Constants for seat prices in each seating section
    SEAT_PRICE_A = 20
    SEAT_PRICE_B = 15
    SEAT_PRICE_C = 10
    # Constants for the number of seats in each section
    SEAT_MAX_A = 300
    SEAT_MAX_B = 500
    SEAT_MAX_C = 200
    # Constant to prevent negative ticket inputs
    SEAT_MIN_ALL = 0
    # Initialize validation loop variables
    validateA = 0
    validateB = 0
    validateC = 0
    
    # Initialize total income variable
    totalIncome = 0

    # Get Section A ticket number and loop until inputs are validated
    while validateA == 0:
        try:
            ticketsSoldA = int(input('Enter the number of tickets sold for Section A seating: '))
            if (ticketsSoldA < SEAT_MIN_ALL) or (ticketsSoldA > SEAT_MAX_A):
                print("Invalid entry for Section A seating capacity")
            else:
                validateA = 1
        except ValueError:
            print("Invalid entry for Section A seating capacity")

    # Get Section B ticket number and loop until inputs are validated
    while validateB == 0:
        try:
            ticketsSoldB = int(input('Enter the number of tickets sold for Section B seating: '))
            if (ticketsSoldB < SEAT_MIN_ALL) or (ticketsSoldB > SEAT_MAX_B):
                print("Invalid entry for Section B seating capacity")
            else:
                validateB = 1
        except ValueError:
            print("Invalid entry for Section B seating capacity")
    
    # Get Section C ticket number and loop until inputs are validated
    while validateC == 0:
        try:
            ticketsSoldC = int(input('Enter the number of tickets sold for Section C seating: '))
            if (ticketsSoldC < SEAT_MIN_ALL) or (ticketsSoldC > SEAT_MAX_C):
                print("Invalid entry for Section C seating capacity")
            else:
                validateC = 1
        except ValueError:
            print("Invalid entry for Section C seating capacity")

    # Calculate and display total income from ticket sales
    totalIncome = (SEAT_PRICE_A * ticketsSoldA) + (SEAT_PRICE_B * ticketsSoldB) + (SEAT_PRICE_C * ticketsSoldC)
    print("Tonight's ticket sales generated a total income of ${:,.2f}".format(totalIncome))

# Program loop
while runAgain == 'y' or runAgain == 'ye' or runAgain == 'yes':
    main() # Call main
    runAgain = input("Do you want to run the program again? (yes/no): ").lower() # Ask if the user wants to run the program again