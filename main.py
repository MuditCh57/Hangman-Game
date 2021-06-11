import pygame
import os
import random

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE =  (255, 127, 0)
PINK =  (235, 52, 198)
GREEN =  (0, 255, 0)
BLUE =  (0, 0, 255)
INDIGO =  (46, 43, 95)
VIOLET =  (139, 0, 255)
color_list = [RED, ORANGE, PINK, GREEN, BLUE, INDIGO, VIOLET]

# Letter Fonts
letter_fonts = pygame.font.SysFont("comicsansms", 24)

# Setup Window
WIDTH, HEIGHT = 900, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Button Variables
GAP = 15
RADIUS = 20
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 450
letters = []
A = 65

for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (RADIUS * 2 + GAP))
    color = random.choice(color_list)
    letters.append([x,y,chr(A + i), color])

# Load Images
images = []
for i in range(0,7):
    image = pygame.image.load(os.path.join("Images/", f"hangman{i}.png"))
    images.append(image)

# Game variables
hangman_img_status = 0

# Draw function
def draw():
    window.fill(WHITE)
    window.blit(images[hangman_img_status], (370, 50))

    # Draw Buttons
    for letter in letters:
        x, y, ltr , clr = letter
        pygame.draw.circle(window, BLACK, (x, y), RADIUS, 2)
        text = letter_fonts.render(ltr, 1, clr)
        window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    pygame.display.flip()

# Game Loop
FPS = 60
clock = pygame.time.Clock()
run = True
while(run):
    clock.tick(FPS)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
