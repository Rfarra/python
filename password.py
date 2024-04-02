def main():
    valid = False
    while not vaild:
        valid = True
        print(
            """ password requirements:\n
            between 8 to 20 characters long.\n
            contains at least one uppercase letter.\n
            contains at least one lowercase.\n
            includes at least one number.\n
            Includes at least one symbol from the set: !@#$%&*\n"""
        )

        password = input("Please eneter a password that meets the criteria")
        length = len(password)
        if 7 < len < 21:
            continue
        else:
            vaild = False
            print("that password is not the right length")

            is_upper = False #change tp true if found
            #for loop stepping through characters in password.Look for upper case

            has_symbol = False
            symbol = ["!", "@", "#"]
            for s in symbol:
                for c in password:
                    if s == c:
                        has_symbol == True
                        if has_symbol == False:
                            print("you need to include a symbol")
                            continue


main()