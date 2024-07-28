import random
import pgzrun

# Constants
FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
START_SPEED = 10
MIN_SPEED = 1  # Minimum speed level
COLORS = ["green", "blue"]

# Game state variables
game_over = False
game_complete = False
current_level = 1
stars = []
animations = []
miss_count = 0  # Tracks misses

def draw():
    global current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0, 0))
    
    if game_over:
        display_message("GAME OVER!", "Press R to Restart.")
    elif game_complete:
        display_message("YOU WON!", "Press R to Restart.")
    else:
        for star in stars:
            star.draw()
        
        # Display current level in the bottom right corner
        screen.draw.text(f"Level: {current_level}", fontsize=30, bottomright=(WIDTH - 10, HEIGHT - 10), color=FONT_COLOR)

def update():
    global stars, current_level, game_over, game_complete, miss_count
    
    if len(stars) == 0:
        stars = make_stars(current_level)

    # Check for game over on 3rd miss
    if miss_count >= 3:
        game_over = True

def make_stars(number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colors_to_create(number_of_extra_stars):
    colors_to_create = ["red"]
    for i in range(0, number_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_stars(colors_to_create):
    new_stars = []
    for color in colors_to_create:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars

def layout_stars(stars_to_layout):
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos

def animate_stars(stars_to_animate):
    global current_level  # Declare current_level as global for modification
    for star in stars_to_animate:
        # Ensure duration doesn't go below MIN_SPEED
        duration = max(START_SPEED - current_level, MIN_SPEED)
        star.anchor = ("center", "bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global stars, current_level, game_complete, miss_count
    clicked_on_star = False
    for star in stars:
        if star.collidepoint(pos):
            clicked_on_star = True
            if "red" in star.image:
                red_star_click()
            else:
                handle_miss()
    if not clicked_on_star:
        handle_miss()

def red_star_click():
    global current_level, stars, animations, game_complete, miss_count
    stop_animations(animations)
    current_level += 1
    stars = []
    animations = []
    miss_count = 0  # Reset miss count on successful click

def handle_miss():
    global miss_count, current_level  # Declare current_level as global for modification
    miss_count += 1
    # Decrease current_level by 1 if not already at MIN_SPEED
    if current_level > MIN_SPEED:
        current_level -= 1

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTER_X, CENTER_Y + 30), color=FONT_COLOR)

def on_key_down(key):
    global game_over, game_complete, current_level, stars, animations, miss_count
    if key == keys.R:
        if game_over or game_complete:
            game_over = False
            game_complete = False
            current_level = 1
            stars = []
            animations = []
            miss_count = 0
            reset_dots()

def reset_dots():
    global stars, current_level
    stars = make_stars(current_level)

pgzrun.go()


'''import random
import pgzrun

# Constants
FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
START_SPEED = 10
MIN_SPEED = 1  # Minimum speed level
COLORS = ["green", "blue"]

# Game state variables
game_over = False
game_complete = False
current_level = 1
stars = []
animations = []
miss_count = 0  # Tracks misses

def draw():
    global current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0, 0))
    
    if game_over:
        display_message("GAME OVER!", "Press R to Restart.")
    elif game_complete:
        display_message("YOU WON!", "Press R to Restart.")
    else:
        for star in stars:
            star.draw()
        
        # Display current level in the bottom right corner
        screen.draw.text(f"Level: {current_level}", fontsize=30, bottomright=(WIDTH - 10, HEIGHT - 10), color=FONT_COLOR)

def update():
    global stars, current_level, game_over, game_complete, miss_count
    
    if len(stars) == 0:
        stars = make_stars(current_level)

    # Check for game over on 3rd miss
    if miss_count >= 3:
        game_over = True

def make_stars(number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colors_to_create(number_of_extra_stars):
    colors_to_create = ["red"]
    for i in range(0, number_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_stars(colors_to_create):
    new_stars = []
    for color in colors_to_create:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars

def layout_stars(stars_to_layout):
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos

def animate_stars(stars_to_animate):
    global current_level  # Declare current_level as global for modification
    for star in stars_to_animate:
        # Ensure duration doesn't go below MIN_SPEED
        duration = max(START_SPEED - current_level, MIN_SPEED)
        star.anchor = ("center", "bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global stars, current_level, game_complete, miss_count
    clicked_on_star = False
    for star in stars:
        if star.collidepoint(pos):
            clicked_on_star = True
            if "red" in star.image:
                red_star_click()
            else:
                handle_miss()
    if not clicked_on_star:
        handle_miss()

def red_star_click():
    global current_level, stars, animations, game_complete, miss_count
    stop_animations(animations)
    current_level += 1
    stars = []
    animations = []
    miss_count = 0  # Reset miss count on successful click

def handle_miss():
    global miss_count, current_level  # Declare current_level as global for modification
    miss_count += 1
    # Decrease current_level by 1 if not already at MIN_SPEED
    if current_level > MIN_SPEED:
        current_level -= 1

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTER_X, CENTER_Y + 30), color=FONT_COLOR)

def on_key_down(key):
    global game_over, game_complete, current_level, stars, animations, miss_count
    if key == keys.R:
        if game_over or game_complete:
            game_over = False
            game_complete = False
            current_level = 1
            stars = []
            animations = []
            miss_count = 0
            reset_dots()

def reset_dots():
    global stars, current_level
    stars = make_stars(current_level)

pgzrun.go()'''


'''import pgzrun
import random

# Constants
FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
COLORS = ["green", "blue"]

# Game state variables
game_over = False
game_complete = False
current_level = 1
stars = []
animations = []

# Draw function to render the screen
def draw():
    global stars, current_level, game_over, game_complete
    screen.clear()
    screen.blit("space", (0, 0))
    if game_over:
        display_message("GAME OVER!", "Try again.")
    elif game_complete:
        display_message("YOU WON!", "Well done.")
    else:
        for star in stars:
            star.draw()

# Update function to manage the game state
def update():
    global stars
    if len(stars) == 0:
        stars = make_stars(current_level)

# Function to create stars based on the current level
def make_stars(number_of_extra_stars):
    colors_to_create = get_colors_to_create(number_of_extra_stars)
    new_stars = create_stars(colors_to_create)
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

# Get colors for the stars
def get_colors_to_create(number_of_extra_stars):
    colors_to_create = ["red"]
    for i in range(0, number_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

# Create star Actors
def create_stars(colors_to_create):
    new_stars = []
    for color in colors_to_create:
        star = Actor(color + "-star")
        new_stars.append(star)
    return new_stars

# Layout stars on the screen
def layout_stars(stars_to_layout):
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos
        star.y = 0

# Animate stars falling down
def animate_stars(stars_to_animate):
    global animations
    for star in stars_to_animate:
        duration = START_SPEED - current_level
        star.anchor = ("center", "bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

# Handle game over state
def handle_game_over():
    global game_over
    game_over = True

# Handle mouse click events
def on_mouse_down(pos):
    global stars, current_level
    for star in stars:
        if star.collidepoint(pos):
            if "red" in star.image:
                red_star_click()
            else:
                handle_game_over()

# Handle red star click
def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        stars = []
        animations = []

# Stop all animations
def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

# Display messages on the screen
def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTER_X, CENTER_Y + 30), color=FONT_COLOR)

# Start the game
pgzrun.go()'''
