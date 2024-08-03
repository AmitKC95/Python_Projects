import csv

studs = []

with open("studs.csv") as file:
    reader = csv.reader(file) #DictReader
    for name, house in reader:
        studs.append({"name": name, "house": house})
        # studs.append({"name": row["name"], "house": row["house"]})


for stud in sorted(studs, key=lambda stud: stud["name"]):
    print(f"{stud['name']} is in {stud['house']}")

'''name = input("What's your name?")
House = input("What's your House?")

with open("studs.csv", "a") as file:
    writer = csv.reader(file)
    writer.writerow(name, house)
'''




'''studs = []

with open("studs.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        stud = {"name": name, "house": house}
        studs.append(stud)

def get_Name(studs):
    return studs["house"]

for studs in sorted(studs, key=get_Name):
    print(f"{stud['name']} is in {stud['house']}")'''





'''studs = []

with open("studs.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        studs.append(f"{name} is in {house}.")

for studs in sorted(studs):
    print(studs)'''




'''with open("studs.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}.")'''
              
        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]} House.")