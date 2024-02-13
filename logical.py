# Get input from the user
num1 = int(input("Enter an integer: "))
num2 = int(input("Enter another integer: "))

# Both numbers greater than 0
print("Both numbers greater than 0:", num1 > 0 and num2 > 0)

# Both numbers greater than 100
print("Both numbers greater than 100:", num1 > 100 and num2 > 100)

# Either number is even
print("Either number is even?", num1 % 2 == 0 or num2 % 2 == 0)

# Either number is less than 100
print("Either number is less than 100?", num1 < 100 or num2 < 100)

# num1 is not equal to num2
print("num1 is not equal to num2:", num1 != num2)

# num1 is not 0
print("num1 is not 0:", not num1 == 0)
