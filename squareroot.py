# create a function that calculates the square root of a number using Newton's method
# newton method: x1 = (x0 + number/x0) / 2
# Author Finian Doonan


def sqrt(number, tolerance=0.0001): # tolerance is the difference between the guess and the actual square root
    if number < 0:
        return None  # Square root of a negative number is not defined for real numbers
    
    guess = number / 2.0  # Initial guess is half the number
    while abs(guess**2 - number) > tolerance: # While the difference between the guess and the actual square root is greater than the tolerance
        guess = (guess + number / guess) / 2.0  # Newton's method formula
    
    return guess

# Main program
def root(): # Function to get user input and call the sqrt function
    try:
        number = float(input("Please enter a positive number: "))
        if number < 0:
            print("error: Please enter a positive number.")
            return
        
        approx_sqrt = sqrt(number)
        print(f"The square root of {number} is approximately {approx_sqrt}.") # Print the result
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    root()
