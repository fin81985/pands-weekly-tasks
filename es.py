# Write a program that reads in a text file and outputs the number of e's it contains.
# The program should take the filename from an argument on the command line.
# Author: Finian Doonan

filename = input("Please enter the file name: ")# input from user
count = 0 # variable to store the count of 'e' in the file

try:# try to open the file
    with open(filename, 'r') as f:# open the file
        for line in f:
            count += line.count('e')# count the number of 'e' in the line

except FileNotFoundError:# deals with the error if the file is not found
    print(f"Error: The file '{filename}' was not found.")

    
print(f"The text '{filename}' contains {count} occurrences of the letter 'e'.")


