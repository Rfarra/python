def main():
   
    current_date_time = input("Enter the current date and time: ")

   
    diary_entry = input("Enter your diary entry: ")

 
    with open("diary.txt", "a") as file:
       
        file.write(current_date_time + "\n")
        
        file.write("\n")
       
        file.write(diary_entry + "\n")
   
        file.write("\n")


if __name__ == "__main__":
    main()
