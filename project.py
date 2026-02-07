# Metro Ticket Booking System

total_seats = 100
available_seats = total_seats

while True:
    print("\n===== METRO TICKET BOOKING SYSTEM =====")
    print("1. Book Ticket")
    print("2. Show Remaining Seats")
    print("3. Cancel Ticket")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        tickets = int(input("Enter number of tickets to book: "))
        if tickets <= available_seats:
            available_seats -= tickets
            print("Tickets booked successfully!")
        else:
            print("Not enough seats available!")

    elif choice == 2:
        print(f"🎫 Remaining seats: {available_seats}")

    elif choice == 3:
        cancel = int(input("Enter number of tickets to cancel: "))
        if available_seats + cancel <= total_seats:
            available_seats += cancel
            print("Tickets cancelled successfully!")
        else:
            print(" Invalid cancellation!")

    elif choice == 4:
        print("Thank you for using Metro Booking System!")
        break

    else:
        print("Invalid choice! Try again.")
