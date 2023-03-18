# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

ht, wt = float(height), int(weight)
bmi = wt / (ht ** ht)

print(f"BMI is: {int(bmi)}")