
# this is a tip calculator to calculate tips on your bill 

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? \n 10,12, or 15? "))

people = int(input("How many people to split the bill? "))

tip_calculations = (total_bill * (tip / 100)  + total_bill) / people

rounded_tip_calculations = round(tip_calculations , 2)

print(f"Each person should pay: ${rounded_tip_calculations}")
