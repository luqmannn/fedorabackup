print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15 percent? "))
people = int(input("How many people to split the bill? "))

tip_to_pay = (tip / 100) * bill
final_bill = tip_to_pay + bill
person_pay = final_bill / people

print(f"Each person should pay: {round(person_pay, 2)}")