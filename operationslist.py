seats = list(range(1, 20))

print("Welcome to the ticket sales system!")

while True:
    print("Available seats:", seats)
    seat_number = input(
        "Enter the seat number you want to purchase (enter '0' to finish): "
    )

    if seat_number == "0":
        print("Thank you for purchasing tickets. Enjoy the event!")
        break

    try:
        seat_number = int(seat_number)
        if seat_number in seats:
            seats.remove(seat_number)
            print(f"Seat {seat_number} successfully purchased.")
        else:
            print("Invalid seat number or already sold. Please choose another seat.")
    except ValueError:
        print("Invalid input. Please enter a valid seat number.")
