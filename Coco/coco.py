import pgzrun
from random import randint

# Screen dimensions
WIDTH = 600
HEIGHT = 600

# Initial game state
score = 0
high_scores = [0, 0, 0]
game_over = False

# Initialize actors
fox = Actor("fox")
fox.pos = 100, 100

coin1 = Actor("coin")
coin1.pos = 200, 200

coin2 = Actor("coin")
coin2.pos = 300, 300

# Load sounds
coin_sound = sounds.coin_collect
game_over_sound = sounds.game_over

# High score file
HIGH_SCORE_FILE = "high_scores.txt"

def draw():
    screen.clear()
    if game_over:
        screen.fill("black")
        screen.draw.text(f"Game Over! Your Final Score: {score}", topleft=(10, 10), fontsize=40)
        screen.draw.text("Press 'R' to Restart", topleft=(10, 80), fontsize=30)
        screen.draw.text("Top 3 Scores:", topleft=(10, 150), fontsize=30)
        for i, hs in enumerate(high_scores):
            screen.draw.text(f"{i+1}. {hs}", topleft=(10, 190 + 40 * i), fontsize=30)
    else:
        screen.fill("green")
        fox.draw()
        coin1.draw()
        coin2.draw()
        screen.draw.text(f"Score: {score}", color="black", topleft=(10, 10))

def place_coins():
    coin1.pos = (randint(20, WIDTH - 20), randint(20, HEIGHT - 20))
    coin2.pos = (randint(20, WIDTH - 20), randint(20, HEIGHT - 20))

def time_up():
    global game_over
    game_over = True
    game_over_sound.play()
    update_high_scores()
    save_high_scores()

def update_high_scores():
    global high_scores
    high_scores.append(score)
    high_scores = sorted(high_scores, reverse=True)[:3]

def save_high_scores():
    with open(HIGH_SCORE_FILE, 'w') as file:
        for score in high_scores:
            file.write(f"{score}\n")

def load_high_scores():
    global high_scores
    try:
        with open(HIGH_SCORE_FILE, 'r') as file:
            high_scores = [int(line.strip()) for line in file.readlines()]
    except FileNotFoundError:
        high_scores = [0, 0, 0]

def update():
    global score, game_over

    if keyboard.r and game_over:
        restart_game()

    if not game_over:
        if keyboard.left:
            animate(fox, pos=(fox.x - 5, fox.y), duration=0.01)
        if keyboard.right:
            animate(fox, pos=(fox.x + 5, fox.y), duration=0.01)
        if keyboard.up:
            animate(fox, pos=(fox.x, fox.y - 5), duration=0.01)
        if keyboard.down:
            animate(fox, pos=(fox.x, fox.y + 5), duration=0.01)

        if fox.colliderect(coin1) or fox.colliderect(coin2):
            score += 10
            coin_sound.play()
            place_coins()

def restart_game():
    global score, game_over
    score = 0
    game_over = False
    place_coins()
    clock.schedule(time_up, 16.0)

# Initial setup
load_high_scores()
place_coins()
clock.schedule(time_up, 16.0)

pgzrun.go()





'''import pgzrun
from random import randint

# Screen dimensions
WIDTH = 400
HEIGHT = 400

# Initial game state
score = 0
high_scores = [0, 0, 0]
game_over = False

# Initialize actors
fox = Actor("fox")
fox.pos = 100, 100

coin1 = Actor("coin")
coin1.pos = 200, 200

coin2 = Actor("coin")
coin2.pos = 300, 300

def draw():
    screen.clear()
    if game_over:
        screen.fill("black")
        screen.draw.text(f"Game Over, Final Score: {score}", topleft=(10, 10), fontsize=40)
        screen.draw.text("Press 'R' to Restart", topleft=(10, 80), fontsize=30)
        screen.draw.text("Top 3 Scores:", topleft=(10, 150), fontsize=30)
        for i, hs in enumerate(high_scores):
            screen.draw.text(f"{i+1}. {hs}", topleft=(10, 190 + 40 * i), fontsize=30)
    else:
        screen.fill("green")
        fox.draw()
        coin1.draw()
        coin2.draw()
        screen.draw.text(f"Score: {score}", color="black", topleft=(10, 10))

def place_coins():
    coin1.pos = (randint(20, WIDTH - 20), randint(20, HEIGHT - 20))
    coin2.pos = (randint(20, WIDTH - 20), randint(20, HEIGHT - 20))

def time_up():
    global game_over
    game_over = True
    update_high_scores()

def update_high_scores():
    global high_scores
    high_scores.append(score)
    high_scores = sorted(high_scores, reverse=True)[:3]

def update():
    global score, game_over

    if keyboard.r and game_over:
        restart_game()

    if not game_over:
        if keyboard.left:
            fox.x -= 5
        if keyboard.right:
            fox.x += 5
        if keyboard.up:
            fox.y -= 5
        if keyboard.down:
            fox.y += 5

        if fox.colliderect(coin1) or fox.colliderect(coin2):
            score += 10
            place_coins()

def restart_game():
    global score, game_over
    score = 0
    game_over = False
    place_coins()
    clock.schedule(time_up, 16.0)

place_coins()
clock.schedule(time_up, 16.0)

pgzrun.go()'''





'''# Import necessary modules
import pgzrun
from random import randint

# Initialize game constants
WIDTH = 600     # Set the width of the game window
HEIGHT = 600    # Set the height of the game window
score = 0       # Initialize player's score
game_over = False

# Create actors: fox and coin
fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = WIDTH // 2, HEIGHT // 2   # Set initial position of the coin

def draw():
    """
    Draw function to render game elements on the screen.
    """
    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)
    else:
        screen.fill("green")
        fox.draw()
        coin.draw()
        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

def place_coin():
    """
    Function to place the coin in a random position on the screen.
    """
    coin.x = randint(50, WIDTH - 50)
    coin.y = randint(50, HEIGHT - 50)

def time_up():
    """
    Function to end the game after a certain time interval.
    """
    global game_over
    game_over = True

def update():
    """
    Update function to handle game logic.
    """
    global score

    # Check for player input to move the fox
    if keyboard.left:
        fox.x -= 4
    elif keyboard.right:
        fox.x += 4
    elif keyboard.up:
        fox.y -= 4
    elif keyboard.down:
        fox.y += 4

    # Check if the fox collects the coin
    if fox.colliderect(coin):
        score += 10
        place_coin()  # Place the coin in a new position after collection

    # Schedule game over after 15 seconds
    clock.schedule(time_up, 15.0)

# Initialize the game by placing the initial coin
place_coin()

# Run the game
pgzrun.go()'''