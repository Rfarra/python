# Define a dictionary to store steps for each day
steps = {
    "Sunday": 5468,
    "Monday": 6587,
    "Tuesday": 9786,
    "Wednesday": 6875,
    "Thursday": 6854,
    "Friday": 5876,
    "Saturday": 5874,
}

# Print the steps for each day
for day, step_count in steps.items():
    print(f"How many steps did you take on {day}? {step_count}")

# Calculate and print total and average steps
total_steps = sum(steps.values())
average_steps = total_steps / len(steps)

print("\nTotal steps:", total_steps)
print("Average steps:", average_steps)
