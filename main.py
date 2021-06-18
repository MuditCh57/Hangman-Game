import pygame
import os
import random
import math
import sys
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOWISH = (252, 186, 3)
ORANGE =  (255, 127, 0)
PINK =  (235, 52, 198)
GREEN =  (0, 255, 0)
BLUE =  (0, 0, 255)
INDIGO =  (46, 43, 95)
VIOLET =  (139, 0, 255)
RED = (255, 0, 0)
color_list = [YELLOWISH, ORANGE, PINK, BLACK, BLUE, INDIGO, VIOLET]

# Letter Fonts
letter_fonts = pygame.font.SysFont("comicsansms", 24)
word_fonts = pygame.font.SysFont("comicsansms", 33)
RESULT_FONT = pygame.font.SysFont("comicsansms", 68)

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
    color = BLACK
    letters.append([x, y, chr(A + i), color])

# Load Images
images = []
for i in range(0,7):
    image = pygame.image.load(os.path.join("Images/", f"hangman{i}.png"))
    images.append(image)

# Word variabes
topics = ["dance","country","animals","sports","food","fruit","cars","jobs","weather"]
words = {"dance": ["ACADEMIES", "ACROBATIC", "ADAGIO", "AFFECT", "BALLET", "BALLROOM", "BAND", "BARRE", "BEARING", "BEAUTY", "BEGUINE", "JAZZ", "JIG", "JITTERBUG", "JOYFUL", "JUMP"]
}
topic = "dance"
word = random.choice(words[topic])
guessed = []
print(word)

# Game variables
hangman_img_status = 0

# Draw function
def draw():
    window.fill(WHITE)
    window.blit(images[hangman_img_status], (60, 60))

    # Draw Buttons
    for letter in letters:
        x, y, ltr , clr = letter
        pygame.draw.circle(window, BLACK, (x, y), RADIUS, 2)
        text = letter_fonts.render(ltr, 1, clr)
        window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    # Draw Words
    display_words = ""
    for letter in word:
        if (letter in guessed):
            display_words += letter + " "
        else:
            display_words += "_ "
    text = word_fonts.render(display_words, 1, BLACK)
    window.blit(text, (400, 200))

    pygame.display.flip()

# Game Loop
FPS = 60
clock = pygame.time.Clock()
def game_loop():
    global hangman_img_status
    win = True
    run = True
    while(run):
        clock.tick(FPS)
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, color = letter
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if (dis < RADIUS and color != RED and color != GREEN):
                        if (ltr not in word):
                            hangman_img_status += 1
                            letter[3] = RED
                        else:
                            letter[3] = GREEN
                        guessed.append(ltr)
        win = True
        for letter in word:
            if letter not in guessed:
                win = False
                break
        if win or hangman_img_status >=6:
            end_game_loop(win)
        # if (hangman_img_status >= 6):
        #     end_game_loop(win)

# Reset the game
def reset():
    global guessed, word, title, hangman_img_status, letters
    guessed.clear()
    title = 'dance'
    word = random.choice(words[topic])
    hangman_img_status = 0
    letters.clear()

    for i in range(26):
        x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = starty + ((i // 13) * (RADIUS * 2 + GAP))
        color = BLACK
        letters.append([x, y, chr(A + i), color])
        
# End Loop for end screen which show result
def end_game_loop(win):
    run = True
    while(run):
        click = False
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        window.fill(WHITE)

        window.blit(images[6], (350, 40))
        # Result text
        if win:
            text = RESULT_FONT.render("You won!!", 1, VIOLET)
        else:
            text = RESULT_FONT.render("You lost!!", 1, VIOLET)
        window.blit(text, (320, 300))

        # Play again button
        rect = pygame.draw.rect(window, RED, (350, 500, 220, 80))
        text = word_fonts.render("Play Again", 1, BLACK)

        # Check if Button is click or not
        m_x, m_y = pygame.mouse.get_pos()
        if rect.x + rect.width > m_x > rect.x and rect.y + rect.height > m_y > rect.y :
            text = word_fonts.render("Play Again", 1, WHITE)
            if click:
                reset()
                run = False
        window.blit(text, (rect.x + text.get_width() / 2 - 40, rect.y + text.get_height() / 2 - 5))

        pygame.display.flip()

if __name__ == "__main__":
    game_loop()