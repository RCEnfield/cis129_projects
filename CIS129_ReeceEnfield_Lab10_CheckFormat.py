# CIS129_ReeceEnfield_Lab10_CheckFormat.py
# Reece Enfield
# April 8, 2024
# This program requests a check dollar amount to be entered then displays the check dollar amount in check-protected format in a field of 10 characters with leading asterisks if necessary

endProgram = 'no' # initialize endProgram variable

while endProgram.lower() == 'no': # loops program functions until user no longer declines the prompt to end the program
     # initialize checkAmount variable
    while True: # validates user input to fit the check format
        try:
            checkAmount = float(input("Enter the check's dollar amount: ")) # gets check's dollar amount from user
        except ValueError:
            print('The value entered was invalid.') # displays error message to user if input did not fit the correct format
        else:
            print(f'{checkAmount:*>10.2f}') # displays the check dollar amount in check-protected format in a field of 10 characters with leading asterisks if necessary
            break
    endProgram = input('Do you want to end program? (yes/no): ') # asks user if they wish to end the program