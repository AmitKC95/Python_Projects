# Define the base class Employee
class Employee:
    def __init__(self, name, age, salary):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute
        self._salary = salary  # Protected attribute

    def display_info(self):
        print(f"Name: {self._name}, Age: {self._age}, Salary: {self._salary}")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


# Define a subclass Manager inheriting from Employee
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self._department = department  # Protected attribute

    def display_info(self):
        super().display_info()
        print(f"Department: {self._department}")

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department


# Define a subclass Developer inheriting from Employee
class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self._programming_language = programming_language  # Protected attribute

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self._programming_language}")

    def get_programming_language(self):
        return self._programming_language

    def set_programming_language(self, programming_language):
        self._programming_language = programming_language


# Create instances of different types of employees
manager = Manager("Alice", 35, 80000, "Operations")
developer = Developer("Bob", 28, 60000, "Python")

# Display information about each employee
print("Manager Information:")
manager.display_info()
print("\nDeveloper Information:")
developer.display_info()

# Change and display updated information using setters and getters
print("\nUpdating Developer Information:")
developer.set_name("Bobby")
developer.set_programming_language("JavaScript")
developer.display_info()
