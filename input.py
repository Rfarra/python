print("Budget Breakdown Calculator!")

# Get user input for total budget
total_budget = float(input("Enter your total budget ($): "))

# where money is spent
categories = {
    "Housing": float(input("Enter amount spent on Housing ($): ")),
    "Utilities": float(input("Enter amount spent on Utilities ($): ")),
    "Groceries": float(input("Enter amount spent on Groceries ($): ")),
    "Transportation": float(input("Enter amount spent on Transportation ($): ")),
    "Health Care": float(input("Enter amount spent on Health Care ($): ")),
}
