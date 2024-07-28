print("Hello, World!")


name = "Alice"
age = 25
height = 5.4
is_student = True

print(name, age, height, is_student)


a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


num = 7

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# For loop
for i in range(5):
    print("For loop iteration:", i)

# While loop
i = 0
while i < 5:
    print("While loop iteration:", i)
    i += 1


def greet(name):
    return "Hello, " + name

print(greet("Alice"))


fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])  # Accessing an element

fruits.append("orange")  # Adding an element
print(fruits)


squares = [x ** 2 for x in range(10)]
print(squares)
cubes = [x ** 3 for x in range(10)]
print(cubes)


student = {"name": "Alice", "age": 25, "is_student": True}
print(student)
print(student["name"])  # Accessing a value

student["age"] = 26  # Modifying a value
print(student)       # students[0]["age"] = 26


point = (3, 4)
print(point)
print(point[0])  # Accessing an element

# point[0] = 5  # This will raise an error as tuples are immutable


colors = {"red", "green", "blue"}
print(colors)

colors.add("yellow")  # Adding an element
print(colors)


name = "Alice"
age = 25

print(f"Name: {name}, Age: {age}")
print("Name: {}, Age: {}".format(name, age))


'''name = input("Enter your name: ")
print("Hello, " + name)'''


# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This runs no matter what.")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("Alice", 25)
print(person.greet())


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.name)
print(dog.speak())


add = lambda x, y: x + y
print(add(3, 5))


from functools import reduce

# Map
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])  # Slicing a list
print(numbers[:5])   # From start to index 5
print(numbers[5:])   # From index 5 to end
print(numbers[::2])  # Every second element


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # Accessing elements in a nested list


fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


text = "hello world"
print(text.upper())       # Convert to uppercase
print(text.capitalize())  # Capitalize first letter
print(text.replace("world", "Python"))  # Replace substring


student = {"name": "Alice", "age": 25, "is_student": True}
print(student.keys())   # Get all keys
print(student.values()) # Get all values
print(student.items())  # Get all key-value pairs


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))        # Union of sets
print(set1.intersection(set2)) # Intersection of sets
print(set1.difference(set2))   # Difference of sets


numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23}
]

students.sort(key=lambda student : student["age"])
print(students)


import random

print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(["apple", "banana", "cherry"]))  # Random choice from a list


numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)


import math

print(math.sqrt(16))   # Square root
print(math.pi)         # PI constant


import datetime

now = datetime.datetime.now()
print(now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Formatted date and time


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

car = Car("Toyota", "Camry", 2020)
print(car.display_info())


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog("Buddy")
print(dog.speak())


def factorial(n):
    # Base Case: When n is 0
    if n == 0:
        return 1
    # Recursive Case: Calls factorial with n-1
    else:
        return n * factorial(n - 1)

print(factorial(5))


'''def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)'''

def generate_fibonacci(limit):
    fib_list = []
    a, b = 0, 1
    while len(fib_list) < limit:
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

fibonacci_list = generate_fibonacci(16)
print(fibonacci_list)


numbers = [1, 2, 3, 4]
squares = (map(lambda x: x ** 2, numbers))
print(list(squares))


numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)


names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

zipped = list(zip(names, ages))
print(zipped)


zipped = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
names, ages = zip(*zipped)
print(names)
print(ages)


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print(flattened)


fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

# Or using slicing
print(numbers[::-1])


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)


squares = {x: x ** 2 for x in range(5)}
print(squares)


with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


lines = ["First line", "Second line", "Third line"]

with open("example.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

print(nested_dict["person1"]["name"])


from collections import defaultdict

d = defaultdict(lambda: "Not present")
d["key1"] = "value1"

print(d["key1"])  # Output: value1
print(d["key2"])  # Output: Not present


max_value = lambda a, b: a if a > b else b
print(max_value(10, 20))


# Original dictionary
data = {'name': 'Course', 'Fees': 12000, 'Duration': '2 Months', 'Course': 'Machine Learning'}

# Remove the duplicate entry
del data['Course']

# Pop the key-value pair for 'name'
value = data.pop('name')

# Insert the key-value pair at the desired position
data = {'Name': 'Machine Learning', **data}

# Display the updated dictionary
print(data)


#51
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)


def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))
print(is_palindrome("hello"))


numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[-3:])


a = 5
b = 10
a, b = b, a
print(a, b)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)


numbers = [1, 2, 3, 4, 5]
print(max(numbers))


numbers = [1, 2, 3, 4, 5]
print(min(numbers))


s = "hello"
print(s[::-1])


words = ["hello", "world"]
sentence = " ".join(words)
print(sentence)


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)


data = {'name': 'Alice', 'age': 25}
print(data.get('name'))
print(data.get('gender', 'Unknown'))


data = {'name': 'Alice', 'age': 25}
for key, value in data.items():
    print(f"{key}: {value}")


numbers = [1, 2, 3, 4, 5]
print(sum(numbers))


squares = [x ** 2 for x in range(10)]
print(squares)


numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)

with open('example.txt', 'r') as file:
    content = file.read()
print(content)


with open('example.txt', 'w') as file:
    file.write("Hello, World!")


numbers = [1, 2, 3, 4, 5]
print(len(numbers))


numbers = [1, 2, 3, 4, 5]
print(numbers.index(3))


#72
