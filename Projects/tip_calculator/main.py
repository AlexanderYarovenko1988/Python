print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $"))
percent = int(input("How much tip would you like to give? 10, 12, or 15? $"))
number_of_people = int(input("How many people to split the bill?"))
tip_percent = total_bill * percent / 100
total_amount = total_bill + (total_bill * percent / 100)
person_amount = round(total_amount / number_of_people, 2)
print(f"Each person should pay: ${person_amount}")


