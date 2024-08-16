import random
import string

# Set to store unique IDs
generated_ids = set()

def generate_unique_user_ids(n, l): 
    characters = string.ascii_letters + string.digits
    
    for _ in range(l):  # Loop l times to generate l unique IDs
        while True:
            random_user_id = ''.join(random.choice(characters) for _ in range(n)) 
            if random_user_id not in generated_ids:
                generated_ids.add(random_user_id)
                print(random_user_id)
                break

# Example
generate_unique_user_ids(6, 3)


# Get user input from terminal
'''
try:
    n = int(input("Enter the length of each user ID: "))
    l = int(input("Enter the number of unique user IDs to generate: "))
    generate_unique_user_ids(n, l)
except ValueError:
    print("Invalid input. Please enter integers only.")'''


'''def generate_unique_user_id(): #--->Use length = 6, then range(length) and final range when calling/printing
    characters = string.ascii_letters + string.digits
    while True:
        random_user_id = ''.join(random.choice(characters) for _ in range(6)) # n in brackets and at time of print add a value for that no. of character length
        if random_user_id not in generated_ids:
            generated_ids.add(random_user_id)
            return random_user_id

print(generate_unique_user_id())

#if n is used in () above, you can add a value here in the brackets
print(generate_unique_user_id())'''

