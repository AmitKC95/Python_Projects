fruits = ['banana', 'orange', 'mango', 'lemon']

new_f = input("Enter a Fruit to the list - ")

if new_f in fruits:
    print(f"{new_f} is already in the Fruits list.\t Enter a different Fruit")
else:
    fruits.append(new_f)
    print(fruits)