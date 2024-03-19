def main():
    # my string
    my_string = "Hello, Python programmers!"

    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    my_string = "hello python programmers"
    for char in my_string:
        print(char, end=" ")

    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")


minimum = min(my_string)
print(min("/" + minimum + " / "))


# TODO: Find and print the character with the maximum ASCII value in the string
print("\nCharacter with the maximum ASCII value:")

print(max(my_string))


# TODO: Find and print the index of the first occurrence of 'o' in the string
print("\nIndex of 'o':")

x = my_string.index("o")
print(x)

# TODO: Convert the string into a list of characters and print the list
print("\nConverting string to a list of characters:")

my_list = list(my_string)
print(my_list)


# TODO: Count and print the number of occurrences of 'o' in the string
print("\nCount of 'o' in the string:")

x = my_string.count("o")
print(x)

main()
