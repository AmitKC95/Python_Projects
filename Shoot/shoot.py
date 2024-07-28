import pgzrun
from random import randint
from time import time

# Initialize the game variables
apple = Actor("apple")
score = 0
game_over = False
start_time = time()
game_duration = 30  # Game duration in seconds

# Function to draw the game elements
def draw():
    screen.clear()
    apple.draw()
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30)
    elapsed_time = int(time() - start_time)
    screen.draw.text(f"Time: {elapsed_time}", topright=(780, 10), fontsize=30)

    if game_over:
        screen.draw.text("Game Over!", center=(400, 300), fontsize=60, color="red")
        screen.draw.text("Press 'R' to Restart", center=(400, 350), fontsize=40, color="white")

# Function to place the apple at a random position
def place_apple():
    apple.x = randint(10, 790)
    apple.y = randint(10, 590)

# Function to handle mouse clicks
def on_mouse_down(pos):
    global score, game_over
    if game_over:
        return

    if apple.collidepoint(pos):
        score += 1
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")

# Function to update the game state
def update():
    global game_over
    elapsed_time = int(time() - start_time)
    if elapsed_time >= game_duration:
        game_over = True

# Function to handle keyboard input
def on_key_down(key):
    global game_over, score, start_time

    if key == keys.R and game_over:
        game_over = False
        score = 0
        start_time = time()
        place_apple()

# Initial placement of the apple
place_apple()

# Start the game loop
pgzrun.go()





'''import pgzrun
from random import randint, choice
from time import time
import json
import os

# Initialize the game variables
apple = Actor("apple")
clock = Actor("clock")
score = 0
misses = 0
game_over = False
start_time = time()
game_duration = 30  # Game duration in seconds
top_scores = []

# File path for storing top scores
directory = "game_folder"
filename = "top_scores.json"
filepath = os.path.join(directory, filename)

# Load top scores from a file
def load_top_scores():
    global top_scores
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            top_scores = json.load(file)
    else:
        top_scores = []

# Save top scores to a file
def save_top_scores():
    global top_scores
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(filepath, 'w') as file:
        json.dump(top_scores, file, indent=4)

# Initialize the game state
def reset_game():
    global score, misses, game_over, start_time
    score = 0
    misses = 0
    game_over = False
    start_time = time()
    place_apple()
    place_clock()

# Function to draw the game elements
def draw():
    global score, misses, game_over
    screen.clear()
    apple.draw()
    clock.draw()
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30)
    screen.draw.text(f"Misses: {misses}", topleft=(10, 40), fontsize=30)
    elapsed_time = max(0, int(game_duration - (time() - start_time)))
    screen.draw.text(f"Time: {elapsed_time}", topright=(780, 10), fontsize=30)

    if game_over:
        screen.draw.text("Game Over!", center=(400, 300), fontsize=60, color="red")
        screen.draw.text("Press 'R' to Restart", center=(400, 350), fontsize=40, color="white")
        screen.draw.text("Top Scores:", center=(400, 400), fontsize=40, color="yellow")
        for i, score in enumerate(top_scores):
            screen.draw.text(f"{i + 1}. {score}", center=(400, 450 + i * 30), fontsize=30, color="yellow")

# Function to place the apple at a random position
def place_apple():
    apple.x = randint(10, 790)
    apple.y = randint(10, 590)

# Function to place the clock at a random position
def place_clock():
    clock.x = randint(10, 790)
    clock.y = randint(10, 590)

# Function to handle mouse clicks
def on_mouse_down(pos):
    global score, misses, game_over, start_time
    if game_over:
        return

    if apple.collidepoint(pos):
        score += 1
        place_apple()
    elif clock.collidepoint(pos):
        start_time += 3  # Add 3 extra seconds
        place_clock()
    else:
        misses += 1

    if misses >= 3:
        game_over = True
        update_top_scores(score)

# Function to update the game state
def update():
    global game_over
    if game_over:
        return

    elapsed_time = int(time() - start_time)
    if elapsed_time >= game_duration:
        game_over = True
        update_top_scores(score)
    else:
        move_clock()

# Function to update the top scores
def update_top_scores(new_score):
    global top_scores
    top_scores.append(new_score)
    top_scores = sorted(top_scores, reverse=True)[:3]
    save_top_scores()

# Function to handle keyboard input
def on_key_down(key):
    if key == keys.R and game_over:
        reset_game()

# Function to move the clock randomly
def move_clock():
    clock.x += randint(-5, 5)
    clock.y += randint(-5, 5)
    clock.x = max(10, min(790, clock.x))
    clock.y = max(10, min(590, clock.y))

# Load top scores and start the game
load_top_scores()
reset_game()
pgzrun.go()'''







'''import pgzrun
from random import randint

apple = Actor("apple")

def draw():
    screen.clear()
    apple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    else:
        print("You missed!")
        quit()

place_apple()
pgzrun.go()'''




'''import pgzrun  

apple = Actor("apple") 

def draw():
    screen.clear()  
    apple.draw()  

apple.width = 50
apple.height = 50


def place_apple():
    apple.x = 600
    apple.y = 400

place_apple()

pgzrun.go()''' 