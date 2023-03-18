# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

print(f"Original data type is: {type(two_digit_number)}")

num1, num2 = int(two_digit_number[0]), int(two_digit_number[1])
total = num1 + num2
print(total)

print(f"Data type after conversion: {type(total)}")

"""
Another solution
num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

print(num1 + num2)
"""
