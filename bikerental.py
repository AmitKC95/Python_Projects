class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def displayBikes(self):
        print("Total Bikes:", self.stock)

    def rentBike(self, quantity):
        if quantity <= 0:
            print("Enter a positive value greater than zero.")
        elif quantity > self.stock:
            print("Enter a value less than or equal to the available stock.")
        else:
            price = quantity * 100  # Assuming each bike costs 100 units
            print("Total Price:", price)
            self.stock -= quantity
            print("Remaining Bikes:", self.stock)

# Main program loop
while True:
    obj = BikeShop(10)  # Initial stock of 10 bikes

    print("\nMenu:")
    print("1. Display Stock")
    print("2. Rent a Bike")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.displayBikes()
    elif choice == 2:
        qty = int(input("Enter the quantity of bikes to rent: "))
        obj.rentBike(qty)
    elif choice == 3:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
