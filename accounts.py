# reads in a 10 character account number and outputs the account number with only the last 4 digits showing 
# Author: Finian Doonan

import math
account = input("Enter your account number: ") # reads in the account number
print("X" * (len(account) - 4) + account[-4:] if len(account) <= math.inf else "Account number is not the correct length") 
# prints out the account number with only the last 4 digits showing if the account number is less than 10 characters long