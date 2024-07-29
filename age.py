my_age = int(29)
your_age = int(input("Enter your Age - "))

age_difference = your_age - my_age

if age_difference > 1:
    print(f"You're older than me by {age_difference} years")
elif age_difference == 1:
    print(f"You're an year older than me, we practically same")
elif age_difference == 0:
    print("We are both same years of age. So you can call me the Fistborn twin!")
# elif 0 > age_difference:
else:
    print(f"I'm older than you by {age_difference} years. So you can call me, Big Brother, Master of you! ")

