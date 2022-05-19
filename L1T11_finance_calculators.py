import math

#I've imported the math module in order to use the functions in the module

print("Choose either 'investment' or 'bond' from the menu below to proceed:\nInvestment - to calculate the amount of interest on you'll earn on investment.\nBond - to calculate the amount of you'll have to pay on a home loan.")
print()

# The above line will help the user to know which calculator they want to use. 
# The below line will allow them to input their selection.

calculator = input("Please enter your selection here: ").casefold()
print()
#I added the ".casefold()" function to the input fields to make the code run regardless of user capitalisation. I figured it out from here: https://www.codegrepper.com/code-examples/python/make+string+not+case+sensitive+python

if calculator == "investment":
    
    deposit_investment = float(input("Please enter the amount you are depositing: "))
    interest_rate_investment = int(input("Please enter your current interest rate (without the '%' sign): "))/100
    years_investing = float(input("How many years do you intend on investing for?: "))
    interest = input("Do you want simple interest or compound interest?: ").casefold()
    
    if interest == "simple":
            simple_interest = float(deposit_investment*(1+interest_rate_investment*years_investing))
            simple = round(simple_interest, 2)
            print(f"Your interest on your investment is R{simple_interest}.")
        
    elif interest == "compound":
            compound_interest = float((deposit_investment)*math.pow((1+interest_rate_investment),years_investing))
            compound = round(compound_interest, 2)
            print(f"Your interest on your investment is R{compound}.")

# The above section of if...elif statements calculate the interest on an investment. 
# This is decided by the user's response to the question above the if statements
# I have first asked the user to enter their deposit amount (what they are investing), their interest rate and how long they intend to invest for.
# I then nested further if and elif statements because I have asked the user to input whether they want to calculate their simple interest or their compound interest.
# Nesting the statements was necessary because the branch of the program needed to grow further.
# I rounded off the final interest rates because it is a monetary value, and cannot contain more than 2 decimal places. 
# I then displayed the result for the user in a sentence.

elif calculator == "bond":
    
    housevalue_bond = float(input("Please enter the current value of your house: R"))
    interest_rate_bond = int(input("Please enter your current interest rate (without the '%' sign): "))/100
    monthly_interest_rate = float((interest_rate_bond/12))
    months_repayment = int(input("How many months will you be repaying your bond over?: "))
    bond_repayment = float(monthly_interest_rate*housevalue_bond)/(1 - (1+monthly_interest_rate)**(-months_repayment))
    bond = round(bond_repayment, 2)
    print(f"Your bond repayments are R{bond} per month.")

# The elif statement above calculates a bond repayment if that was their response to the question above the first if statement.
# I have asked the user to input the value of their house, the interest rate on their bond and the number of months they wish to repay the bond over.
# I have then divided the interest rate by 12 in order to work out what the monthly interest rate is.
# I have rounded the final bond repayment to 2 decimal places because it is a monetary value and then displayed the amount for the user.

else:
    print("You have not entered a valid option. Please try again.")

# The else statement above asks the user to please try again to input only "bond" or "investment"
# I have added ".casefold()" to all input fields to make the user's response case insensitive.

# I made the final interest and the bond repayments floats so that the calculations would be accurate after the division and multiplication. 
# This is because interest rates are represented by a fraction.