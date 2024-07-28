import random

def throw_water_balloon():
    while True:
        print("\nWelcome to the Water Balloon Game!\n")
        print("Pick an option:")
        print("1. In a hurry, surprise me!")
        print("2. Pick a water balloon")
        print("3. End game")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            # Surprise option
            options = ['Water balloon', 'Water balloon with paint', 'Popped balloon', 'Egg']
            surprise = random.choice(options)

            if surprise == 'Egg':
                print("Surprise! You got an egg! Prepare for some fun...")
            else:
                print(f"Surprise! You got a {surprise}.")

            # Throw at random friends
            friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Gina', 'Hannah']
            target = random.choice(friends)
            hit = random.random() < 0.8  # 80% chance of hitting

            if hit:
                print(f"You hit {target}! They got wet!")
                if surprise == 'Egg':
                    print(f"Oh no! {target} got angry...")
                    revenge = random.random() < 0.5  # 50% chance of revenge hit
                    if revenge:
                        print(f"{target} retaliates! They hit you back!")
                    else:
                        print(f"{target} calms down this time.")
            else:
                print(f"Oops, you missed {target}. Better luck next time!")

        elif choice == '2':
            # Regular water balloon options
            print("Pick a water balloon:")
            print("1. Water only")
            print("2. Water with paint")
            print("3. Return to main menu")

            balloon_choice = input("Enter your choice (1-3): ").strip()

            if balloon_choice == '1':
                print("You picked a water balloon with only water inside.")
            elif balloon_choice == '2':
                print("You picked a water balloon with paint inside.")
            elif balloon_choice == '3':
                continue
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

            # Throw at random friends
            friends = ['Amit', 'Sumit', 'Yati', 'Sahil', 'Moksh', 'Tanya']
            target = random.choice(friends)
            hit = random.random() < 0.8  # 80% chance of hitting

            if hit:
                print(f"You hit {target}! They got wet!")
            else:
                print(f"Oops, you missed {target}. Better luck next time!")

        elif choice == '3':
            print("Thanks for playing! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

        # Ask if want to play again
        play_again = input("\nDo you want to throw another water balloon? (y/n): ").strip().lower()
        if play_again != "y":
            print("\nAww, maybe next time! Come back again soon for more fun.")
            break

# Start the game
throw_water_balloon()
