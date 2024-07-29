import json

# Data to be written to JSON
data = {
    'Course_Name': 'Python',
    'Fees': 15000
}

# Writing JSON data to a file
with open('data.json', 'w') as file:
    json.dump(data, file)

print("Data has been written to data.json")
