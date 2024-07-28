import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Shapes of Tetrominos
SHAPES = [
    [[1, 1, 1, 1]],              # I shape
    [[1, 1, 1], [0, 1, 0]],      # T shape
    [[1, 1, 1], [1, 0, 0]],      # L shape
    [[1, 1, 1], [0, 0, 1]],      # J shape
    [[0, 1, 1], [1, 1, 0]],      # S shape
    [[1, 1, 0], [0, 1, 1]],      # Z shape
    [[1, 1], [1, 1]]             # O shape
]

# Colors corresponding to Tetrominos
COLORS = [
    (0, 255, 255),    # Cyan for I
    (128, 0, 128),    # Purple for T
    (255, 165, 0),    # Orange for L
    (0, 0, 255),      # Blue for J
    (0, 255, 0),      # Green for S
    (255, 0, 0),      # Red for Z
    (255, 255, 0)     # Yellow for O
]

# Initialize game variables
grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
current_shape = None
current_color = None
current_x, current_y = GRID_WIDTH // 2, 0
score = 0
game_over = False

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Functions

def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = grid[y][x]
            if color > 0:
                pygame.draw.rect(screen, COLORS[color - 1],
                                 (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, WHITE,
                             (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def new_shape():
    global current_shape, current_color, current_x, current_y
    shape_index = random.randint(0, len(SHAPES) - 1)
    current_shape = SHAPES[shape_index]
    current_color = COLORS[shape_index]
    current_x = GRID_WIDTH // 2 - len(current_shape[0]) // 2
    current_y = 0

def draw_shape():
    for y in range(len(current_shape)):
        for x in range(len(current_shape[y])):
            if current_shape[y][x] == 1:
                pygame.draw.rect(screen, current_color,
                                 ((current_x + x) * GRID_SIZE, (current_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(screen, WHITE,
                                 ((current_x + x) * GRID_SIZE, (current_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

def check_collision():
    global current_x, current_y, current_shape, grid, game_over
    for y in range(len(current_shape)):
        for x in range(len(current_shape[y])):
            if current_shape[y][x] == 1:
                if current_y + y >= GRID_HEIGHT or current_x + x < 0 or current_x + x >= GRID_WIDTH or grid[current_y + y][current_x + x] > 0:
                    if current_y == 0:
                        game_over = True
                    else:
                        for y1 in range(len(current_shape)):
                            for x1 in range(len(current_shape[y1])):
                                if current_shape[y1][x1] == 1:
                                    grid[current_y + y1 - 1][current_x + x1] = len(current_color)

                        check_line()
                        new_shape()
    return game_over

def check_line():
    global score
    lines = 0
    for y in range(GRID_HEIGHT):
        if all(grid[y]):
            lines += 1
            for y1 in range(y, 1, -1):
                for x1 in range(GRID_WIDTH):
                    grid[y1][x1] = grid[y1 - 1][x1]
            grid[0] = [0] * GRID_WIDTH
    score += lines * 10

def draw_score():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (20, 20))

def main():
    global current_x, current_y, grid, game_over

    clock = pygame.time.Clock()

    while not game_over:
        screen.fill(BLACK)
        draw_grid()
        draw_shape()
        draw_score()
        pygame.display.update()

        current_y += 1
        if check_collision():
            game_over = True
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_x -= 1
                    if check_collision():
                        current_x += 1
                elif event.key == pygame.K_RIGHT:
                    current_x += 1
                    if check_collision():
                        current_x -= 1
                elif event.key == pygame.K_DOWN:
                    current_y += 1
                    if check_collision():
                        current_y -= 1
                elif event.key == pygame.K_UP:
                    current_shape = rotate_shape(current_shape)
                    if check_collision():
                        current_shape = rotate_shape(current_shape)
                    pygame.time.wait(100)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        clock.tick(10)

    pygame.quit()

def rotate_shape(shape):
    return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]

if __name__ == "__main__":
    new_shape()
    main()
