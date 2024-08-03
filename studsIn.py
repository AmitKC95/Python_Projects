import csv

name = input("What's your name?")
house = input("What's your House?")

with open("studs.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"name" : name, "house" : house})