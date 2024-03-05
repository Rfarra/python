def factorial(n):
    #code for function
    if n==0 or n==1:
     return 1
    else:
     return n * factorial(n - 1)

def main():
    number = int(input("Enter a non-negative integer: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print("The factorial of", number, "is", factorial(number))


