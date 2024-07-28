import pgzrun
from random import randint
import time

WIDTH = 400
HEIGHT = 400

dot_connect_sound = sounds.zoom_in
dot_disconnect_sound = sounds.zoom_out
level_up_sound = sounds.level_up

dots = []
lines = []
next_dot = 0
level = 1
dots_per_level = 4

start_time = 0
current_time = 0
timer_running = False

def reset_dots():
    global dots, lines, next_dot, start_time, timer_running, level, dots_per_level
    dots = []
    lines = []
    next_dot = 0
    for dot in range(dots_per_level + (level - 1) * 2):
        actor = Actor("dot")
        actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        dots.append(actor)
    start_time = 0
    timer_running = False

reset_dots()

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 16))
        dot.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

    if timer_running:
        current_time = time.time() - start_time
        screen.draw.text(f"Time: {current_time:.2f} seconds", (10, 10), fontsize=30, color="white")
    screen.draw.text(f"Level: {level}", (WIDTH - 100, 10), fontsize=30, color="white")

def on_mouse_down(pos):
    global next_dot, lines, current_time, start_time, timer_running, level
    if not timer_running:
        start_time = time.time()
        timer_running = True

    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        dot_connect_sound.play()
        next_dot += 1
        if next_dot == len(dots):
            current_time = time.time() - start_time
            timer_running = False
            level_up_sound.play()
            print(f"Level {level} complete! Time: {current_time:.2f} seconds")
            level += 1
            reset_dots()
    else:
        dot_disconnect_sound.play()
        lines = []
        next_dot = 0
        reset_dots()

pgzrun.go()


'''import pgzrun
from random import randint
import time

WIDTH = 600
HEIGHT = 600

dot_connect_sound = sounds.zoom_in
dot_disconnect_sound = sounds.zoom_out

dots = []
lines = []
next_dot = 0

# Timer
start_time = 0
current_time = 0
timer_running = False

# Reset dots and start the timer
def reset_dots():
    global dots, lines, next_dot, start_time, timer_running
    dots = []
    lines = []
    next_dot = 0
    for dot in range(10):
        actor = Actor("coin")
        actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        dots.append(actor)
    start_time = 0
    timer_running = False

reset_dots()

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 25))
        dot.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

    # Display timer if running
    if timer_running:
        current_time = time.time() - start_time
        screen.draw.text(f"Time: {current_time:.2f} seconds", (10, 10), fontsize=30, color="white")

def on_mouse_down(pos):
    global next_dot, lines, current_time, start_time, timer_running
    if not timer_running:
        start_time = time.time()
        timer_running = True

    if dots[next_dot].collidepoint(pos):
        if next_dot:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        dot_connect_sound.play()
        next_dot += 1
        if next_dot == len(dots):
            current_time = time.time() - start_time
            timer_running = False
            print(f"Round complete! Time: {current_time:.2f} seconds")
            reset_dots()
    else:
        dot_disconnect_sound.play()
        lines = []
        next_dot = 0
        reset_dots()

pgzrun.go()'''










'''import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

dot_connect_sound = sounds.zoom_in
dot_disconnect_sound = sounds.zoom_out

dots = []
lines = []
next_dot = 0

# Function to initialize or reset dots
def initialize_dots():
    global dots, lines, next_dot
    dots = []
    lines = []
    next_dot = 0
    for dot in range(10):
        actor = Actor("dot")
        actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        dots.append(actor)

# Initialize dots for the first time
initialize_dots()

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1

    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

def on_mouse_down(pos):
    global next_dot
    global lines

    if dots[next_dot].collidepoint(pos):
        dot_connect_sound.play()
        if next_dot > 0:
            lines.append((dots[next_dot - 1].pos, dots[next_dot].pos))
        next_dot += 1
        if next_dot == 10:
            print("All dots connected! Resetting...")
            initialize_dots()
    else:
        dot_disconnect_sound.play()
        print("Failed! Resetting...")
        initialize_dots()

pgzrun.go()'''