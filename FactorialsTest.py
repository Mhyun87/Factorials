"""
the mathmatical definition of n! for n>0 is 1*2*...*n
this module tests the factorialNonRecursive(n) and factorialRecursive(n) functions
it defines the main function
then it provides the call to the main function
"""

#import the factorialNonRecursive(n) and factorialRecursive(n) in the Factorials.py file
from Factorials import *

def main():
    """
    n! main program
    n! = 1*2*...*n
    """
    print("n! calculation")
    print("")
    
    number = input("Enter a whole number between 1 and 100 or a blank string when finished: ")
    while number != "":
        n = int(number)
        if (n<1 or n>100):
            print("Invalid entry")
        else:
            print("n! calculated by non-recursive technique: ", factorialNonRecursive(n) )
            print("n! calculated by recursive technique:     ", factorialRecursive(n) )
        print("")
        number = input("Enter a whole number between 1 and 100 or a blank string when finished: ")

    # hold window open to allow user to view output
    print("")
    input("Press ENTER to continue ")

# call main()
if __name__ == "__main__":
    main()


