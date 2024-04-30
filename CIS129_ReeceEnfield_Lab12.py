# CIS129_ReeceEnfield_Lab12.py
# Reece Enfield
# April 29, 2024
# This program defines a class named Pet with methods that store and return values indicating the name, type, and age of the pet. The program additionally makes use of the Pet class to request user input of the name, type, and age values to be displayed.

# Main module
def main():

    # Declare input variables
    inputName = input("Enter your pet's name:\n")
    inputType = input("Enter your pet's type:\n")
    inputAge = int(input("Enter your pet's age:\n"))
    
    # Create a Pet object
    Animal = Pet()
    
    # Get values for a pet
    Animal.setName(inputName)
    Animal.setType(inputType)
    Animal.setAge(inputAge)
    
    # Show values for this pet
    print("Your pet's name is", Animal.getName())
    print("Your pet's type is", Animal.getType())
    print("Your pet's age is", Animal.getAge())

# Pet class
class Pet:

    # Constructor
    def __init__(self, n="", t="", a=0):

        # Initialize fields
        self.name = n
        self.type = t
        self.age = a  

    # Mutators
    def setName(self, n):

        # Store the name of the pet
        self.name = n
    
    def setType(self, t):

        # Store the type of the pet
        self.type = t
    
    def setAge(self, a):

        # Store the age of the pet
        self.age = a
    
    # Accessors
    def getName(self):

        # Return the name of the pet
        return self.name
    
    def getType(self):

        # Return the type of the pet
        return self.type
    
    def getAge(self):

        # Return the age of the pet
        return self.age

# Polymorphic call of the main function
if __name__ == "__main__":
    main()