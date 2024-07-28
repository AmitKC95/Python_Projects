import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED = 5
PADDLE_SPEED = 10

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Define Paddle and Ball classes
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 100))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, y):
        self.rect.y += y
        # Ensure paddle stays within screen bounds
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = BALL_SPEED
        self.speed_y = BALL_SPEED

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off the top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y = -self.speed_y

        # Reset ball if it goes off the left or right side
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.rect.center = (WIDTH // 2, HEIGHT // 2)
            self.speed_x = -self.speed_x

# Create instances
player_paddle = Paddle(WIDTH - 20, HEIGHT // 2 - 50)
opponent_paddle = Paddle(10, HEIGHT // 2 - 50)
ball = Ball()

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player_paddle, opponent_paddle, ball)

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_paddle.move(-PADDLE_SPEED)
    if keys[pygame.K_DOWN]:
        player_paddle.move(PADDLE_SPEED)

    # Move the ball
    ball.update()

    # Check for collisions with paddles
    if pygame.sprite.collide_rect(ball, player_paddle) or pygame.sprite.collide_rect(ball, opponent_paddle):
        ball.speed_x = -ball.speed_x

    # Move opponent paddle
    if ball.rect.y < opponent_paddle.rect.y:
        opponent_paddle.move(-PADDLE_SPEED)
    if ball.rect.y > opponent_paddle.rect.y + opponent_paddle.rect.height:
        opponent_paddle.move(PADDLE_SPEED)

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
