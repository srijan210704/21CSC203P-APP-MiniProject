import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, arrival_time, price, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.capacity = capacity
        self.reserved_seats = 0

    def display_flight_info(self):
        return (
            f"Flight Number: {self.flight_number}\n"
            f"From: {self.origin} To: {self.destination}\n"
            f"Departure Time: {self.departure_time}\n"
            f"Arrival Time: {self.arrival_time}\n"
            f"Price: ₹{self.price}\n"
            f"Available Seats: {self.capacity - self.reserved_seats}\n"
        )

    def book_seat(self):
        if self.reserved_seats < self.capacity:
            self.reserved_seats += 1
            return "booked"
        else:
            return "full"

    def calculate_total_fare(self, num_seats):
        return self.price * num_seats

class ReservationSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_available_flights(self):
        available_flights = []
        for flight in self.flights:
            if flight.reserved_seats < flight.capacity:
                available_flights.append(flight.display_flight_info())
        return available_flights

    def book_flight(self, flight_number, num_seats):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                result = flight.book_seat()
                if result == "booked":
                    total_fare = flight.calculate_total_fare(num_seats)
                    return total_fare
                else:
                    return "full"
        return "not_found"

class FlightReservationGUI:
    def __init__(self, root, reservation_system):
        self.root = root
        self.root.title("Flight Reservation System")
        self.reservation_system = reservation_system

        # Load the background image for the reservation window
        background_image = Image.open("C:\Users\SRIJAN\OneDrive\Desktop\Flight Reservation System\reservationbg.jpg")
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(root, image=background_photo)
        background_label.image = background_photo
        background_label.place(relwidth=1, relheight=1)

        self.label = tk.Label(root, text="Flight Reservation System", font=("Helvetica", 20), bg="sky blue")
        self.label.pack(pady=10)

        self.available_flights_label = tk.Label(root, text="Available Flights", font=("Helvetica", 16), bg="light green")
        self.available_flights_label.pack()

        self.available_flights_text = tk.Text(root, height=10, width=40, font=("Helvetica", 12))
        self.available_flights_text.pack()

        self.book_label = tk.Label(root, text="Enter Flight Number to Book:", font=("Helvetica", 16), bg="light yellow")
        self.book_label.pack()

        self.flight_number_entry = tk.Entry(root, font=("Helvetica", 14))
        self.flight_number_entry.pack()

        self.seats_label = tk.Label(root, text="Number of Seats:", font=("Helvetica", 16), bg="light yellow")
        self.seats_label.pack()

        self.seats_entry = tk.Entry(root, font=("Helvetica", 14))
        self.seats_entry.pack()

        self.total_fare_label = tk.Label(root, text="Total Fare (₹):", font=("Helvetica", 16), bg="light yellow")
        self.total_fare_label.pack()

        self.total_fare_var = tk.StringVar()
        self.total_fare_label_value = tk.Label(root, textvariable=self.total_fare_var, font=("Helvetica", 14))
        self.total_fare_label_value.pack()

        self.book_button = tk.Button(root, text="Book Flight", command=self.book_flight, font=("Helvetica", 14), bg="light blue")
        self.book_button.pack(pady=10)

        self.payment_label = tk.Label(root, text="Payment Options", font=("Helvetica", 16), bg="light yellow")
        self.payment_label.pack()

        self.payment_method = tk.StringVar()
        self.payment_method.set("Credit Card")

        payment_options = ["Credit Card", "Debit Card", "Net Banking"]
        for option in payment_options:
            tk.Radiobutton(root, text=option, variable=self.payment_method, value=option, font=("Helvetica", 14), bg="light yellow").pack()

        self.pay_button = tk.Button(root, text="Pay Now", command=self.process_payment, font=("Helvetica", 14), bg="light blue")
        self.pay_button.pack()

        self.display_available_flights()

    def display_available_flights(self):
        available_flights = self.reservation_system.get_available_flights()
        self.available_flights_text.delete(1.0, tk.END)
        for flight_info in available_flights:
            self.available_flights_text.insert(tk.END, flight_info)
            self.available_flights_text.insert(tk.END, "\n\n")

    def book_flight(self):
        flight_number = self.flight_number_entry.get()
        num_seats = int(self.seats_entry.get())
        result = self.reservation_system.book_flight(flight_number, num_seats)
        if isinstance(result, int):
            self.total_fare_var.set(result)
            messagebox.showinfo("Booking Successful", f"Seat(s) booked successfully.\nTotal Fare: ₹{result}")
            self.display_available_flights()
        elif result == "not_found":
            messagebox.showerror("Booking Error", "Flight not found.")
        else:
            messagebox.showerror("Booking Error", "Flight is fully booked")

    def process_payment(self):
        total_fare = self.total_fare_var.get()
        payment_method = self.payment_method.get()
        if not total_fare:
            messagebox.showerror("Payment Error", "Total fare is not available.")
        else:
            messagebox.showinfo("Payment Successful", f"Payment of ₹{total_fare} via {payment_method} successful.")
        self.exit()

    def exit(self):
        self.root.destroy()

class LoginGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        # Load the background image for the login window
        background_image = Image.open(background_image = Image.open(r"C:\Users\SRIJAN\OneDrive\Desktop\Flight Reservation System\loginbg2.jpg")
)
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(root, image=background_photo)
        background_label.image = background_photo
        background_label.place(relwidth=1, relheight=1)

        self.label = tk.Label(root, text="Login", font=("Helvetica", 20))
        self.label.pack(pady=10)

        self.username_label = tk.Label(root, text="Username", font=("Helvetica", 16))
        self.username_label.pack()

        self.username_entry = tk.Entry(root, font=("Helvetica", 14))
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password", font=("Helvetica", 16))
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*", font=("Helvetica", 14))
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login, font=("Helvetica", 14), bg="light green")
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "Srijan" and password == "srijan21":
            self.root.destroy()
            self.open_flight_reservation()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    def open_flight_reservation(self):
        root = tk.Tk()
        reservation_system = ReservationSystem()
        app = FlightReservationGUI(root, reservation_system)

        # Add the provided flights to the reservation system
        flight1 = Flight("AI101", "Mumbai", "Delhi", "08:00 AM", "11:00 AM", 5000, 150)
        flight2 = Flight("IND202", "Bangalore", "Kolkata", "09:30 AM", "01:30 PM", 4500, 200)
        flight3 = Flight("Jet303", "Chennai", "Hyderabad", "10:45 AM", "01:15 PM", 3800, 100)
        flight4 = Flight("Spice404", "Delhi", "Mumbai", "08:30 AM", "11:30 AM", 5200, 120)
        flight5 = Flight("Vistara505", "Kolkata", "Chennai", "10:00 AM", "01:00 PM", 4700, 180)
        flight6 = Flight("GoAir606", "Hyderabad", "Bangalore", "11:15 AM", "02:00 PM", 3900, 160)

        reservation_system.add_flight(flight1)
        reservation_system.add_flight(flight2)
        reservation_system.add_flight(flight3)
        reservation_system.add_flight(flight4)
        reservation_system.add_flight(flight5)
        reservation_system.add_flight(flight6)

        app.display_available_flights()
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginGUI(root)
    root.mainloop()
