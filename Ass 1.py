class Passenger:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def book_flight(self, flight):
        # Implement logic to book a flight for the passenger
        pass

    def make_payment(self, amount):
        # Implement logic to make a payment for the booking
        pass


class Flight:
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time):
        self.flight_number = flight_number
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    def get_flight_number(self):
        return self.flight_number

    def set_flight_number(self, flight_number):
        self.flight_number = flight_number

    def get_departure_airport(self):
        return self.departure_airport

    def set_departure_airport(self, departure_airport):
        self.departure_airport = departure_airport

    def get_arrival_airport(self):
        return self.arrival_airport

    def set_arrival_airport(self, arrival_airport):
        self.arrival_airport = arrival_airport

    def get_departure_time(self):
        return self.departure_time

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def get_arrival_time(self):
        return self.arrival_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_flight_details(self):
        # Implement logic to get flight details
        pass


class Booking:
    def __init__(self, booking_number, passenger_name, flight_number, seat_number):
        self.booking_number = booking_number
        self.passenger_name = passenger_name
        self.flight_number = flight_number
        self.seat_number = seat_number

    def get_booking_number(self):
        return self.booking_number

    def set_booking_number(self, booking_number):
        self.booking_number = booking_number

    def get_passenger_name(self):
        return self.passenger_name

    def set_passenger_name(self, passenger_name):
        self.passenger_name = passenger_name

    def get_flight_number(self):
        return self.flight_number

    def set_flight_number(self, flight_number):
        self.flight_number = flight_number

    def get_seat_number(self):
        return self.seat_number

    def set_seat_number(self, seat_number):
        self.seat_number = seat_number

    def get_booking_details(self):
        # Implement logic to get booking details
        pass


class Payment:
    def __init__(self, payment_id, amount, payment_method):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_method = payment_method

    def get_payment_id(self):
        return self.payment_id

    def set_payment_id(self, payment_id):
        self.payment_id = payment_id

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_payment_method(self):
        return self.payment_method

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self):
        # Implement logic to process payment
        pass


class AirlineStaff:
    def __init__(self, staff_id, name, role):
        self.staff_id = staff_id
        self.name = name
        self.role = role

    def get_staff_id(self):
        return self.staff_id

    def set_staff_id(self, staff_id):
        self.staff_id = staff_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_role(self):
        return self.role

    def set_role(self, role):
        self.role = role

    def update_flight_details(self, flight):
        # Implement logic to update flight details
        pass


class Notification:
    def __init__(self, notification_id, content):
        self.notification_id = notification_id
        self.content = content

    def get_notification_id(self):
        return self.notification_id

    def set_notification_id(self, notification_id):
        self.notification_id = notification_id

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content

    def send_notification(self):
        # Implement logic to send notification
        pass
# Create Passenger object
passenger = Passenger(name="James Smith", email="james@example.com", phone="123-456-7890")

# Create Flight object
flight = Flight(flight_number="NA4321", departure_airport="Chicago ORD", arrival_airport="New York JFK",
                departure_time="06 DEC 20 11:40", arrival_time="06 DEC 20 13:30")

# Create Booking object
booking = Booking(booking_number="629", passenger_name="James Smith", flight_number="NA4321", seat_number="09A")

# Create Payment object
payment = Payment(payment_id="5A6BCD78", amount=0, payment_method="N/A")

# Create AirlineStaff object
airline_staff = AirlineStaff(staff_id="ABC123", name="John Doe", role="Flight Operations")

# Create Notification object
notification = Notification(notification_id="DEF456", content="Flight NA4321 schedule has been updated.")

# Update payment amount
payment.set_amount(500)  # Assuming the ticket price is $500

# Display boarding pass details
print("BOARDING PASS")
print("Passenger:", passenger.get_name())
print("From:", flight.get_departure_airport())
print("To:", flight.get_arrival_airport())
print("Flight:", flight.get_flight_number())
print("Date:", flight.get_departure_time())
print("Time:", flight.get_departure_time())
print("Seat:", booking.get_seat_number())
print("Electronic ticket:", booking.get_booking_number())
print("Gate: 03")
print("Boarding till:", "06 DEC 20 11:20")
print("Arrival time:", flight.get_arrival_time())
print("Terminal: 2")
print("Please be at the gate at boarding time")
