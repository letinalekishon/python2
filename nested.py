# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."
credit_score=int(input("enter credit_score"))
annual_income = int(input("Enter your annual income: "))

if credit_score >700:
    if annual_income >50000:
        print("loan approved")
    else:
        print("Income requirement not met")
else:
    print("Credit_score too low")        


