# Prompt user to enter five names and store them in a list
names = [input(f"Enter name {i + 1}: ") for i in range(5)]

# Sort the list using Bubble Sort algorithm
names.sort()

# Reverse the sorted list
names.reverse()

# Print the final reversed list
print("Reversed sorted list of names:")
print(names)
