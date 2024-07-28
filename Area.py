
import math
Radius = 45
Area = math.pi * Radius ** 2
Circum = (math.pi * 2) * Radius

print(f"(Area of the Circle is : {Area:.2f} square metres, and /n Circumference of the Circle is : {Circum:.2f} metres)")

'''Radius = int(input("Enter your new Radius here"))
Area = Area = math.pi * Radius ** 2
print(f"Area of the new Cirlce is : {Area:.2f} square metres")'''

Length = 10
Width = 20
Area_Rec = Length * Width
print('Area of Rectangle: ', Area_Rec)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75                  # in Kg
volume = 0.075             # in cubic meter
density = mass / volume    # 1000 Kg/m^3
print('Density of the Liquid is - ', density, "Kg/m^3")