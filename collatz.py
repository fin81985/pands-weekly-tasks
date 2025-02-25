# This program will take a positive integer as input and output the Collatz sequence for that number.
# Author: Finian Doonan


def collatz(number):
    if number % 2 == 0:
        return number // 2  # If the number is even, return this value
    else:                               # If the number is odd, return this value
        return 3 * number + 1        # If the number is odd, return this value
    
try:
    number = int(input("Enter a positive integer: "))  # Ask the user to input a positive integer
    while number != 1:  # While the number is not equal to 1
        number = collatz(number)  # Call the collatz function on the number
        print(number)  # Print the number
except ValueError: # If the user enters a non-integer value, print this message8
    print("invalid input.")   # If the user enters a non-integer value, print this message