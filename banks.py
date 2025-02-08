#banks.py
#prompt the user and read in two money amounts (cents)
#add the two amounts
#print out the answer in a human readable format with euro sign and decimal point between the euro and cent amounts
#Author: Finian Doonan

amount1 = int(input("Please enter the first amount: ")) #prompt the user to enter the first amount
amount2 = int(input("Please enter the second amount: ")) #prompt the user to enter the second amount

total_cent = amount1 + amount2 #adds the two amounts together

euro = total_cent /100 #converts the total amount to euro

print(f"The total amount is: €{euro}") #prints out the total amount in euro
