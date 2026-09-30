import random
from datetime import datetime, timedelta
flights = {
    1: {
        "flight_no": "AI101",
        "from": "Delhi",
        "to": "Mumbai",
        "date": "2025-12-01",
        "price": 5500,
        "seats": 30
    },
    2: {
        "flight_no": "AI202",
        "from": "Mumbai",
        "to": "Bangalore",
        "date": "2025-12-02",
        "price": 4500,
        "seats": 25
    },
    3: {
        "flight_no": "AI303",
        "from": "Delhi",
        "to": "Goa",
        "date": "2025-12-05",
        "price": 6000,
        "seats": 20
    },
    4: {
        "flight_no": "AI404",
        "from": "Bangalore",
        "to": "Chennai",
        "date": "2025-12-03",
        "price": 4000,
        "seats": 40
    }
}
cart_flights = []
cart_prices = []
def view_flights():
    print("\nAvailable Flights:")
    print("--------------------------------------------------")
    for key, data in flights.items():
        print(f"{key}. {data['flight_no']} | {data['from']} → {data['to']} | Date: {data['date']} | Price: ₹{data['price']} | Seats: {data['seats']}")
    print("--------------------------------------------------")
def search_flights():
    print("\nSearch Flights By:")
    print("1. Destination")
    print("2. Date")
    choice = input("Enter choice: ")
    if choice == "1":
        dest = input("Enter destination city: ").capitalize()
        print("\nMatching Flights:")
        for key, data in flights.items():
            if data["to"].capitalize() == dest:
                print(f"{key}. {data['flight_no']} | {data['from']} → {data['to']} | {data['date']} | ₹{data['price']}")
    elif choice == "2":
        date = input("Enter date (YYYY-MM-DD): ")
        print("\nMatching Flights:")
        for key, data in flights.items():
            if data["date"] == date:
                print(f"{key}. {data['flight_no']} | {data['from']} → {data['to']} | {data['date']} | ₹{data['price']}")
    else:
        print("Invalid choice.")
def add_to_cart():
    view_flights()
    try:
        choice = int(input("Enter flight number to add to cart: "))
        if choice in flights:
            cart_flights.append(flights[choice]["flight_no"])
            cart_prices.append(flights[choice]["price"])
            print("Flight added to cart successfully!")
        else:
            print("Invalid flight ID.")
    except:
        print("Enter a valid number.")
def remove_from_cart():
    if not cart_flights:
        print("\nCart is empty.")
        return
    print("\nYour Cart:")
    for i, item in enumerate(cart_flights):
        print(f"{i+1}. {item} - ₹{cart_prices[i]}")
    try:
        choice = int(input("Enter item number to remove: "))
        cart_flights.pop(choice - 1)
        cart_prices.pop(choice - 1)
        print("Item removed!")
    except:
        print("Invalid input.")
def show_cart():
    if not cart_flights:
        print("\nCart is empty.")
        return
    print("\nYour Cart Summary:")
    print("-----------------------------")
    for i, item in enumerate(cart_flights):
        print(f"{i+1}. {item} - ₹{cart_prices[i]}")
    print("-----------------------------")
    print("Total Cost: ₹", sum(cart_prices))
def checkout():
    if not cart_flights:
        print("\nCart is empty. Add flights before checkout.")
        return
    print("\nEnter Passenger Details:")
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    address = input("Address: ")
    today = datetime.now().strftime("%Y-%m-%d")
    random_days = random.randint(3, 7)
    est_date = (datetime.now() + timedelta(days=random_days)).strftime("%Y-%m-%d")
    print("\n------ BOOKING CONFIRMATION ------")
    print(f"Passenger: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print("\nFlights Booked:")
    for item in cart_flights:
        print("→", item)
    print("\nTotal Amount: ₹", sum(cart_prices))
    print("Booking Date:", today)
    print(f"Estimated Travel Date  {est_date}")
    print("----------------------------------")
    with open("flight_booking_receipt.txt", "w", encoding="utf-8") as file:
        file.write("------ BOOKING RECEIPT ------\n")
        file.write(f"Passenger: {name}\nAge: {age}\nEmail: {email}\nAddress: {address}\n")
        file.write("\nFlights Booked:\n")
        for item in cart_flights:
            file.write(f"→ {item}\n")
        file.write(f"\nTotal Amount: ₹{sum(cart_prices)}\n")
        file.write(f"Booking Date: {today}\n")
        file.write(f"Travel Date: {est_date}\n")
        file.write("------------------------------")
    print("\nReceipt saved as flight_booking_receipt.txt")
    print("Booking Successful!")
while True:
    print("\n========== FLIGHT BOOKING SYSTEM ==========")
    print("1. View Flights")
    print("2. Search Flights")
    print("3. Add to Cart")
    print("4. Remove from Cart")
    print("5. Show Cart")
    print("6. Checkout")
    print("7. Exit")
    user_choice = input("Enter choice: ")
    if user_choice == "1":
        view_flights()
    elif user_choice == "2":
        search_flights()
    elif user_choice == "3":
        add_to_cart()
    elif user_choice == "4":
        remove_from_cart()
    elif user_choice == "5":
        show_cart()
    elif user_choice == "6":
        checkout()
    elif user_choice == "7":
        print("Thank you for using the Flight Booking System!")
        break
    else:
        print("Invalid choice, try again.")
