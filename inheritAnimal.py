
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass  # 

# Define a subclass Dog, inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Define another subclass Cat, inheriting from Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Define another subclass Bird, inheriting from Animal
class Bird(Animal):
    def make_sound(self):
        return "Chirp!"

# Main code
if __name__ == "__main__":
    # Create instances of different animals
    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    bird = Bird("Tweetie")

    # Make each animal make its sound
    print(f"{dog.name} says: {dog.make_sound()}")
    print(f"{cat.name} says: {cat.make_sound()}")
    print(f"{bird.name} says: {bird.make_sound()}")
