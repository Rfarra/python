class InvalidInputError(Exception):
    # Custom exception implementation

def main():
    while True:
        try:
            user_input=input("please enter a number:")
        except InvalidInputError:
           InvalidInputError as e:
        else:
             print("Valid input.")
        finally:
           (end of program))

    main()