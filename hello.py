def hello(to="world"):
    print("hello,", to)

hello
# Ask user for their name 
name = input ("What's your name? ").strip().title()

# Split user's name into first and last name
first, last = name.split(" ")

hello(name)
print(f"hello, {first}")
