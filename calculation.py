def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate as a whole number (5% would be 5): "))
    time = int(input("Enter the investment time in whole years: "))

    interest = calculate_simple_interest(principal, rate, time)
    total_amount = principal + interest

    print(
        f"The simple interest for a principal amount of ${principal:.2f} at an interest rate of {rate}% over a period of {time} years is: ${interest:.2f}"
    )
    print(f"The total amount after {time} years will be: ${total_amount:.2f}")


if __name__ == "__main__":
    main()
