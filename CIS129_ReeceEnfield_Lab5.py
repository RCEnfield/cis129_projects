# Module 5 Lab-5
# Reece Enfield
# February 26, 2024
# This program takes user input to calculate a total number of bottles collected after a 7-day period as well as the total payout of those accumulated bottles

# Lab 5 The Bottle Return Program

# Step 1: Declare variables below
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'

# Step 2: Loop to run program again
while keepGoing == 'y':
    # Step 3: Code to set value of variables
    totalBottles = 0
    counter = 1
    todayBottles = 0
    totalPayout = 0

    for counter in range (1,8):
        print('Enter number of bottles for day #',counter,':')
        todayBottles = int(input())
        counter += 1
        # code to set value of variable totalBottles
        totalBottles += todayBottles

        # code to set value of variable totalPayout
        totalPayout = totalBottles * .10

    # code to print the number of total bottles and total payout
    print('The total number of bottles collected is',totalBottles)
    print(f'The total paid out is $ {totalPayout:.1f}')

    print("Do you want to enter another week's worth of data?")
    keepGoing = input("(Enter y or n): ")