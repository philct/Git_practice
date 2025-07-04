class flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seat():
            return False
        else:
             self.passengers.append(name)
             return True

    def open_seat(self):
        return self.capacity - len(self.passengers)

Capacity = 3
flight1 = flight(Capacity)
passengers = ["Alice", "Bob", "Charlie", "David"]

for passenger in passengers:
    success = flight1.add_passenger(passenger)
    if success:
        print(f"{passenger} added to flight successfully")
    else:
        print(f"No available seats for {passenger}")