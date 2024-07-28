class DC:
    a = 10  # Class attribute

    # Constructor
    def __init__(self):
        print("Welcome to Kunju Munji's Computer")

    # Method to show value 1
    def showvalue1(self):
        self.c = self.a * self.a  # Using the class attribute 'a'
        print(self.c)

    # Method to show value 2
    def showvalue2(self, a, b):
        print(a + b)

# Creating an object of the class DC
obj = DC()

# Calling the methods
obj.showvalue1()  # Correct method call
obj.showvalue2(20, 30)  # Correct method call with arguments
