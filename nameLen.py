
first_name = 'Python'
last_name = 'Dragon'

x = len(first_name)
y = len(last_name)

print(f"{first_name} is {x} characters long whereas {last_name} is {y} characters long")
print(float(x))
print(str(x))


if x > y:
   print("Hence, Length of {First Name} is bigger, and by ", x-y, "characters")
elif x < y:
   print("Hence, Length of {Last Name} is bigger, and by", y-x, "characters")
else:
    print(f"Both {first_name} and {last_name} are of equal character length")

y = 'on' in first_name and 'on' in last_name
print(y, f", There is 'on' in both {first_name} & {last_name}")

z = not ('on' in first_name and 'on' in last_name)
print(z, f", There is 'on' in both {first_name} & {last_name}")

    
s = 'I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.'
m = 'jargon' in s
print(m)
