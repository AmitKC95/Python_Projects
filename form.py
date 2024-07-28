# Function to display the table
def display_table():
    print("N  1  N  N^2  N^3")
    for i in range(1, 6):
        print(f"{i}  1  {i}  {i**2}  {i**3}")

# Display the table
display_table()



print('I hope everyone is enjoying the Python Challenge.\nAre you ?')
print("Days \tTopics \tExercises")
print("Day 1 \t 5 \t 5")
print("Day 2 \t 6 \t 20")
print("Day 3 \t 5 \t 23")
print("Day 4 \t 1 \t 35")



'''The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s", "%d", "%f", "%.number of digitsf".

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision'''

# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"




first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))




a = 'Coding'
b = 'For'
c = 'All'

Company = (f"{a} {b} {c}")
print(Company)
print(len(Company))
print(Company[0])
print(Company[10])
print(len(Company) -1)



Company = Company.upper()
print(Company)

Company = Company[1:]
print(Company)

'''Company = Company[::-1]
print(Company)'''

if 'Coding' in Company:
    print(True)
else:
    print(False)

Company = Company.replace("ODING", "Python")
Company = Company.replace("ALL", "Everyone")
print(Company)

Company_split = Company.split()
print(Company_split)

CS = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
CSS = CS.split(',')
print(CSS)



pyth = 'Python For Everyone'
calls = 'Coding for All'

acronym = ''.join(word[0] for word in pyth.split())
print(acronym)

acronymalls = ''.join(word[0] for word in calls.split())
print(acronymalls)

sentence = 'You cannot end a sentence with because because because is a conjunction'
position = sentence.find('because')
print(position)


print("Name\tAge\tCountry\tCity")
print("Amit\t29\tIndia\tGurgaon")


import math

radius = 10
area = (math.pi) * radius ** 2

print(f"The Area of Circle with Radius {radius} metres is {area} metres square.")


a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))


fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 

print(rest)           # ['lemon','lime','apple']

# syntax
lst = ['item1', 'item2']
lst.insert(index, item)

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)


# syntax
lst = ['item1', 'item2']
lst.remove(item)

# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)

# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely

