random


def main():
  
    target_number = random(1, 100)

    print("Welcome to the Guess the Number game!")
    print("I've picked a number between 1 and 100. Can you guess it?")

   
    guess = None


    guess = target_number
try:
       
            guess = int(input("enter your guess (between 1 and 100): "))

        
            difference = abs(guess - target_number)

          
            if difference <= 5:
                print("very hot")
            elif difference <= 15:
                print("warm")
            elif difference <= 25:
                print("Cool")
            else:
                print("very cold")
except:
            print("Please enter a valid number.")

   
            print(f"you guessed the number {target_number} correctly!")


