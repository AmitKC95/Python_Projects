print( )
print("functions are fun".count("fun"))
print("blue".upper())

countdown = [1, 2, 3]
countdown.reverse()
print(countdown)

message = "Coding makes me happy"
print(message)
message = message.replace("happy", ":D")
print(message)

'''def fruit_score():
    print(10)
fruit_score()

def fruit_score(fruit):
    if fruit == "apple":
        print(10)
    elif fruit == "orange":
        print(5)

# Calling the function with different parameters
fruit_score("apple")
fruit_score("orange")

user_fruit = input("Enter a fruit (apple or orange): ")
    print(fruit_score)'''

def fruit_score(fruit):
    if fruit == "apple":
        return 10
    elif fruit == "orange":
        return 5
    else:
        return 0  # Return 0 for unknown fruits or handle accordingly

fruit_score("apple")  # This will print 10
fruit_score("orange")  # This will print 5

user_fruit = input("Enter a fruit (apple or orange): ")
print(fruit_score(user_fruit))  # Print the score for the fruit entered by the user

apple_score = fruit_score("apple")
orange_score = fruit_score("orange")
total = fruit_score("apple") + fruit_score("orange")
print(total)

player_name = "Martin"
print("Welcome " + player_name)

