
# Name: Owen Schlagenhaft
# Lab1.py

# Problem: A program that assists the user in showing their monthly interest

# Certification of Authenticity:
# I certify that this assignment is entirely my own work.

annual_Interest = eval(input("What is your Annual Interest"))
billcycle_Days = eval(input("How many days are in your billing cycle"))
previous_Bal = eval(input("How much was your previous Net Balance?"))
payment_Amount = eval(input("How much is your payment amount?"))
billing_Day = eval(input("What day is your payment on?"))

annual_Interest = annual_Interest / 100
payment_Total = (previous_Bal * billcycle_Days)
payment_days = payment_Amount * (billcycle_Days - billing_Day)
payment_Total3 = payment_Total - payment_days
avg_balance = payment_Total3 / billcycle_Days
monthly_rate = round(avg_balance * (annual_Interest / 12),2)
print("Your Monthly Interest is: $", monthly_rate)
