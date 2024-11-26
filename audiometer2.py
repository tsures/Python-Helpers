import pygame
import random

# אתחול pygame
pygame.init()

# הגדרות המסך
WIDTH = 400
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("מד עוצמה")

# צבעים
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# הגדרות המד
BAR_WIDTH = 50
BAR_HEIGHT = 200
BAR_X = WIDTH // 2 - BAR_WIDTH // 2
BAR_Y = HEIGHT - BAR_HEIGHT - 20

# לולאת המשחק
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # סימולציה של קריאת עוצמה (במקום זה תוכל להכניס את הלוגיקה האמיתית שלך)
    strength = random.randint(0, 100)

    # חישוב גובה המד
    bar_height = int((strength / 100) * BAR_HEIGHT)

    # ציור המסך
    screen.fill(BLACK)
    
    # ציור המד
    pygame.draw.rect(screen, RED, (BAR_X, BAR_Y + BAR_HEIGHT - bar_height, BAR_WIDTH, bar_height))
    
    # ציור מסגרת למד
    pygame.draw.rect(screen, RED, (BAR_X, BAR_Y, BAR_WIDTH, BAR_HEIGHT), 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()