import pygame
import os

pygame.init()
# Colors
WHITE = (255, 255, 255)

# Setup Window
WIDTH, HEIGHT = 900, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# Load Images
images = []
for i in range(0,7):
    image = pygame.image.load(os.path.join("Images/", f"hangman{i}.png"))
    images.append(image)

# Game variables
hangman_img_status = 0

# Game Loop
FPS = 60
clock = pygame.time.Clock()
run = True
while(run):
    clock.tick(FPS)
    window.fill(WHITE)
    window.blit(images[hangman_img_status], (370, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()

pygame.quit()
