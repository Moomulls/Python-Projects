import math

# Ask the user to select their choice and display descriptions of options.

choice = input("Choose either 'investment' or 'bond' from the menu below to proceed: "
      "\n \nInvestment - To calculate the amount of interest you'll earn on an investment. "
      "\nBond       - To calculate the amount you'll have to pay on a home loan. \n")

# Create a while loop to prompt the user to use a correct input when no correct response is given.

while choice.upper() != "INVESTMENT" and choice.upper() != "BOND":
      choice = input("Input not recognised, please enter 'investment' or 'bond'. ")

# Use an if statement to separate the two different choices.
# Ask the user a series of questions to collect the relevant information.
# Calculate and print the outcome.

if choice.upper() == "INVESTMENT":
      deposit_amount = int(input("What is the amount you want to deposit? £"))
      interest_rate = int(input("What percentage is the interest rate? "))
      interest_rate = interest_rate / 100
      years = int(input("How many years do you plan on investing? "))

      interest_choice = input("Would you like 'simple' or 'compound' interest? ")

      while interest_choice.upper() != "SIMPLE" and interest_choice.upper() != "COMPOUND":
            interest_choice = input("You entered and incorrect response. Please enter 'simple' or 'compound'. ")

      if interest_choice.upper() == "SIMPLE":
            invest_simple_total = deposit_amount * (1 + interest_rate * years)
            print(f"After {years} years, your total will be £{round(invest_simple_total , 2)}")

      elif interest_choice.upper() == "COMPOUND":
            invest_compound_total = deposit_amount * math.pow((1 + interest_rate), years)
            print(f"After {years} years, your total will be £{round(invest_compound_total , 2)}.")


elif choice.upper() == "BOND":
      house_value = int(input("What is the current value of the house? £"))
      interest_rate_house = int(input("What percentage is the interest rate? "))
      interest_rate_house = interest_rate_house / 100
      months = int(input("How many months would you like to repay? "))
      monthly_interest = interest_rate_house / 12
      repayment = (monthly_interest * house_value) / (1 - math.pow(1 + monthly_interest, - months))
      print(f"Your monthly repayments till be £{round(repayment , 2)}.")