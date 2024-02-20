# Define times of day for heart rate readings
times_of_day = ["Morning", "Afternoon", "Evening", "Night"]

# Initialize empty list to store heart rate readings
heart_rates = []

# Collect heart rate readings for each time of day
for time in times_of_day:
    rate = int(input(f"Enter your heart rate for {time}: "))
    heart_rates.append(rate)

# Calculate average heart rate
average_rate = round(sum(heart_rates) / len(heart_rates))

# Print the average heart rate
print("Your average heart rate is:", average_rate)
