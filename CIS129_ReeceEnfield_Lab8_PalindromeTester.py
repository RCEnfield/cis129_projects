# CIS129_ReeceEnfield_Lab8_PalindromeTester.py
# Reece Enfield
# March 25, 2024
# This program requests for a word to be entered and evaluates whether or not it is a palindrome.

# Defines palindrome detection function
def is_palindrome(string):
    string = string.lower() # Causes function to ignore case sensitivity for palindrome detection

    if string == string[::-1]: # Reverses the string and compares to the original string for palindrome detection
        return True
    else:
        return False

endProgram = 'no'

while endProgram.lower() == 'no':
    string = str(input("Enter a word to test if it is a palindrome: ")) # Requests user input for palindrome testing

    # Calls is_palindrome fucntion for palindrome test
    if is_palindrome(string) == True:
        print(string,"is a palindrome.")
    else:
        print(string,"is not a palindrome")
    
    endProgram = input('Do you want to end program? (yes/no): ')