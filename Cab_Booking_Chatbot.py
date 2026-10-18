import random

while True:
    print("\n========== CAB BOOKING CHATBOT ==========")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        # Select cab type
        print("\nSelect Cab Type:")
        print("1. Auto - Rs.12/km")
        print("2. Sedan - Rs.18/km")
        print("3. SUV - Rs.25/km")

        cab_choice = input("Enter cab choice: ")

        if cab_choice == "1":
            cab_type = "Auto"
            rate = 12
        elif cab_choice == "2":
            cab_type = "Sedan"
            rate = 18
        elif cab_choice == "3":
            cab_type = "SUV"
            rate = 25
        else:
            print("Invalid cab choice! Returning to main menu.")
            continue

        # Select predefined route
        print("\nSelect Route:")
        print("1. Pune Station -> Shivajinagar (5 km)")
        print("2. Swargate -> Kothrud (8 km)")
        print("3. Hinjawadi -> Wakad (10 km)")

        route_choice = input("Enter route choice: ")

        if route_choice == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route_choice == "2":
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif route_choice == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid route choice! Returning to main menu.")
            continue

        # Calculate fare
        fare = rate * distance

        print("\n========== RIDE DETAILS ==========")
        print("Cab Type:", cab_type)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "/km")
        print("Total Fare: Rs.", fare)

        # Confirm or cancel booking before OTP
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm_choice = input("Enter your choice: ")

        if confirm_choice == "1":

            # Generate a four-digit OTP
            otp = random.randint(1000, 9999)

            print("\nYour OTP has been shared:", otp)
            print("Booking Confirmed Successfully!")
            print("IMPORTANT: Ride cancellation is NOT allowed after OTP sharing.")

        elif confirm_choice == "2":
            print("\nRide cancelled successfully.")
            print("No OTP has been shared.")

        else:
            print("Invalid choice! Booking cancelled. No OTP has been shared.")

    elif choice == "2":
        print("\nThank you for using Cab Booking Chatbot!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice! Please select 1 or 2.")