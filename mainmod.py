# mainmod.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, Person as p, gravity as g

# Create an instance of the Person class
amit = p('Amit', 'Chutani')

# Use the instance method to generate the full name
print(amit.generate_full_name())

print(total(1, 9))

mass = 100
weight = mass * g()

print(weight)
print(amit.firstname)
