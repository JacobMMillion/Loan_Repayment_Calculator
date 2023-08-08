# This program is for users with loans who care more about
# understanding when they will be paid off with a certain 
# monthly payment, as oppposed to paying a certain "minimum payment"
# this will allow users to determine how long it will take for a loan
# to be paid off given a set monthly payment

# use auto-py-to-exe to convert this to an executable file

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# setting up the chart
plt.title("Loan Repayment Calculator")
plt.xlabel("Time in Months")
plt.ylabel("Loan Balance")
x_axis = []
y_axis = []

# define the loan class
class Loan:
    balance = 0
    interest_rate = 0
    name = "default"

# allows the user to add all of their loans to the list 'loans'
loans = []
numLoans = 0
print("One by one, please enter your loan information.")
while( True ):
    Amt = int( input("Please enter balance on this loan: ") )
    intRate = float( input("Please enter the interest rate associated with this loan (as a decimal): "))
    name = input("Please enter loan name: ")
    loan = Loan()
    loan.balance = Amt
    loan.interest_rate = intRate
    loan.name = name
    loans.append(loan)

    hasLoan = input("True or False, do you have another loan you would like to enter? ")
    if( hasLoan.lower() != 'true' ):
        for loan in loans:
            print("Loan amount: ", loan.balance)
            print("Loan interest rate: ", loan.interest_rate)
            print("Loan name: ", loan.name)
            print("-------------")
        correct = input("Does this look correct? True or False: ")
        if( correct.lower() == 'true' ):
            break
        else:
            print("Please begin again.")
            exit()

monthly_payment = float (input("Please enter the monthly payment you would like to use for calculations: "))

# now we have been given all the information we need about the loans
# we enter repayment calculations
months = 1
while( True ):

    loan_index = 0
    temp_monthly_payment = monthly_payment / len(loans)

    # each iteration of this for loop represents a month
    for loan in loans:

        monthly_interest = loan.balance * (loan.interest_rate / 12)
        loan.balance -= (temp_monthly_payment - monthly_interest)

        # if the loan is paid off, we remove it
        if( loan.balance <= 0 ): 
            print("-",loan.name, " is paid off after ", months/12.0, " years!")
            del loans[loan_index]

        loan_index += 1

    # adding the data for matplotlib
    x_axis.append(months)
    remainingBalance = 0
    for loan in loans:
        remainingBalance += loan.balance
    y_axis.append(remainingBalance)

    months += 1

    if( len(loans) == 0 ): break

print("You have paid the loans off after: ", months/12.0, " years.")

plt.plot(x_axis, y_axis)
plt.show()

print("Save this file to see the graph!")
