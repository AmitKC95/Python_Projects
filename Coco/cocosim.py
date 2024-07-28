import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
game_over = False
score = 0


fox = Actor("fox")
fox.pos = 100, 100

coin1 = Actor("coin")
coin1.pos = 200, 200

coin2 = Actor("coin")
coin2.pos = 300, 300

coin_sound = sounds.coin_collect
game_over_sound = sounds.game_over


def draw():
    screen.clear()
    if game_over:
        screen.fill("black")
        screen.draw.text(f"Game Over! Your Final Score : {score}", topleft=(10, 10), fontsize=40)
        screen.draw.text("Press 'R' to Restart", topleft=(10, 80), fontsize=30)
    else:
        screen.fill("green")
        fox.draw()
        coin1.draw()
        coin2.draw()
        screen.draw.text(f"Score : {score}", color="black", topleft=(10, 10))

def place_Actors():
    coin1.pos = (randint(20, WIDTH -20), randint(20, HEIGHT -20))
    coin2.pos = (randint(20, WIDTH -20), randint(20, HEIGHT -20))
    
def time_up():
    global score, game_over
    game_over = True
    game_over_sound.play()

def update():
    global score, game_over
    
    if keyboard.r and game_over:
        restart_game()
        
    if not game_over:
        if keyboard.left:
            fox.x = max(fox.x -5, 0)
        if keyboard.right:
            fox.x = min(fox.x +5, WIDTH)
        if keyboard.up:
            fox.y = max(fox.y -5, 0)
        if keyboard.down:
            fox.y = min(fox.y +5, HEIGHT)
        if fox.colliderect(coin1) or fox.colliderect(coin2):
            score += 10
            coin_sound.play()
            place_Actors()
            
def restart_game():
    global score, game_over
    score = 0
    game_over = False
    place_Actors()
    clock.schedule(time_up, 16.0)

place_Actors()
clock.schedule(time_up, 16.0)
    
pgzrun.go()

'''import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600
score = 0
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

def draw():
    screen.clear()
    if game_over:
        screen.fill("black")
        screen.draw.text(f"Game Over! Your Final Score: {score}", topleft=(10, 10), fontsize=40)
        screen.draw.text("Press 'R' to Restart", topleft=(10, 80), fontsize=30)
    else:
        screen.fill("green")
        fox.draw()
        coin1.draw()
        coin2.draw()
        screen.draw.text(f"Score: {score}", color="black", topleft=(10, 10))

def place_actors():
    coin1.pos = (randint(20, WIDTH - 20), randint(20, HEIGHT - 20))
    coin2.pos = (randint(20, WIDTH - 20), randint(20, HEIGHT - 20))

def time_up():
    global game_over
    game_over = True
    game_over_sound.play()

def update():
    global score, game_over

    if keyboard.r and game_over:
        restart_game()

    if not game_over:
        if keyboard.left:
            fox.x = max(fox.x - 5, 0)
        if keyboard.right:
            fox.x = min(fox.x + 5, WIDTH)
        if keyboard.up:
            fox.y = max(fox.y - 5, 0)
        if keyboard.down:
            fox.y = min(fox.y + 5, HEIGHT)

        if fox.colliderect(coin1) or fox.colliderect(coin2):
            score += 10
            coin_sound.play()
            place_actors()

def restart_game():
    global score, game_over
    score = 0
    game_over = False
    place_actors()
    clock.schedule(time_up, 16.0)

# Initial setup
place_actors()
clock.schedule(time_up, 16.0)

pgzrun.go()'''