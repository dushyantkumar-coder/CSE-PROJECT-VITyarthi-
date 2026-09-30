# Flight Booking System (Python)

This is a simple console-based Flight Booking System written in Python. It allows users to:

* View available flights
* Search flights by destination or date
* Add flights to a cart
* Remove flights from the cart
* View cart summary
* Checkout and generate a booking receipt

The project is beginner‑friendly and demonstrates basic Python concepts like dictionaries, lists, functions, file handling, and loops.

##  Features

### 1. View Flights

Displays a list of all available flights with details such as:

* Flight number
* Origin → Destination
* Date
* Price
* Available seats

### 2. Search Flights

You can search flights based on:

* Destination city
* Travel date (YYYY-MM-DD)

### 3. Add to Cart

Choose a flight ID to add it to your cart for booking.

### 4. Remove from Cart

Remove selected flights from the cart.

### 5. Show Cart Summary

Displays:

* Selected flights
* Individual prices
* Total amount payable

### 6. Checkout

During checkout, the user enters passenger details:

* Name
* Age
* Email
* Address

A **booking receipt** is then generated and saved as:

flight_booking_receipt.txt


The receipt includes:

* Passenger details
* Booked flights
* Total price
* Booking date
* Auto‑generated estimated travel date

### **7. Exit**

Ends the program.


##  Receipt Example (Generated File)


------ BOOKING RECEIPT ------

Passenger: John Doe

Age: 28

Email: john@gmail.com

Address: Delhi, India


Flights Booked:

→ AI101

Total Amount: ₹5500

Booking Date: 2025-11-23

Travel Date: 2025-11-27


##  Technologies Used

* Python 3
* Modules:
  
  * random – to generate estimated travel date
  * datetime – to get today’s date and calculate future dates

##  How to Run the Program

1. Copy the Python code into a file, e.g.:flight_booking_system.py
2. Open a terminal/command prompt.
3. Run the program: python flight_booking_system.py
4. Follow the on-screen menu.

##  Notes

* This is a beginner‑level console app.
* No real flight database or API is used.
* Seat count does not decrease after booking (can be added as an enhancement).

##  Possible Improvements

* Store flight and passenger data in a database.
* Add seat selection.
* Decrease available seat count after booking.
* Add password-protected admin panel.
* Implement a GUI (Tkinter / PyQt).
* Add real‑time validation for input fields.
