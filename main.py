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
ORANGE = (255, 127, 0)
PINK = (235, 52, 198)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (46, 43, 95)
VIOLET = (139, 0, 255)
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
for i in range(0, 7):
    image = pygame.image.load(os.path.join("Images/", f"hangman{i}.png"))
    images.append(image)

# Word variabes
topics = ["dance", "finance"]

words = {"dance": ['ACROBATIC', 'ADAGIO', 'AFFECT', 'ALLEMANDE', 'APPRECIATION', 'ART', 'ARTISTIC', 'ATTRIBUTE', 'AUDIENCE', 'AUTHENTIC', 'BALLET', 'BALLROOM', 'BAND', 'BARRE', 'BEARING', 'BEAUTY', 'BEGUINE', 'BLEND', 'BODY', 'BOLERO', 'BOP', 'BORN TO', 'BOW', 'BUFF', 'BUNNY HOP', 'CAKEWALK', 'CANCAN', 'CELEBRATION', 'CHARACTERISTIC', 'CHARLESTON', 'CHOREOGRAPHY', 'CLASSES', 'CLASSICAL', 'CLOCKWISE', 'CLOG', 'COLLABORATIVE', 'COMMUNICATION', 'COMPETENT', 'COMPLEX', 'COMPOSITION', 'CONGA', 'COSTUMES', 'COTILLION', 'CRAFT', 'CULTURAL', 'CULTURE', 'CURTSY', 'DECOR', 'DELICATE', 'DESCRIPTION', 'DESIGN', 'DEVELOP', 'DEVOTION', 'DIP', 'DIRECTION', 'DIRECTOR', 'DISCO', 'EFFECT', 'EFFECTIVE', 'EFFORT', 'EFFORTLESS', 'ELEGANCE', 'EMOTE', 'EMOTION', 'ENERGY', 'ENTERTAINMENT', 'EXERCISE', 'EXPERIMENTAL', 'EXPERTISE', 'EXPRESSIVE', 'EXTRAORDINARY', 'FACILITY', 'FANDANGO', 'FASHIONABLE', 'FEATURED', 'FLAMENCO', 'FLING', 'FLOOR', 'FORM', 'FORMAL', 'FOX TROT', 'FREE', 'FREQUENCY', 'FUNCTION', 'FUNDS', 'FUTURE', 'GARMENT', 'GAVOTTE', 'GESTURE', 'GLIDE', 'GRACE', 'GRANT', 'GROUPS', 'GYMNASIUM', 'HORA', 'HULA', 'IDEAL', 'IMITATION', 'IMPROVISE', 'INDIVIDUALITY', 'INFORMAL', 'INSPIRATION', 'INSPIRED BY', 'INTERPRET', 'INTERPRETATION', 'JAZZ', 'JIG', 'JITTERBUG', 'JOYFUL', 'JUMP', 'KIND', 'LEAP', 'LEOTARD', 'LIFT', 'LIGHT', 'LINE', 'MAJOR', 'MAKE UP', 'MAMBO', 'MASTERY', 'MAYPOLE', 'MAZURKA', 'MINOR', 'MINUET', 'MIX', 'MONEY', 'MOOD', 'MOTION', 'MOVEMENT', 'MOVIES', 'MUSIC', 'MUSICAL', 'MUSICALITY', 'NOVICE', 'NUMBERS', 'ORCHESTRA', 'ORGANIZED', 'ORIGINAL', 'PARTNER', 'PASSION', 'PATTERNS', 'PENCHANT', 'PERSON', 'PIECE', 'POLKA', 'PORTRAY', 'POSITION', 'POSTURE', 'POWERFUL', 'PRACTICE', 'PRECISION', 'PRESSURE', 'PRIMITIVE', 'PRODUCTION', 'PROGRAM', 'PROPORTION', 'PURPOSE', 'QUADRILLE', 'QUALITY', 'QUICK', 'RECREATION', 'REEL', 'REHEARSAL', 'REHEARSE', 'REVEL', 'REVELATION', 'RHYTHM', 'RISE', 'ROLE', 'ROTATION', 'SHUFFLE', 'SPACE', 'SPECTACLE', 'SPECTATOR', 'SPEED', 'STAR', 'STEPS', 'STRUT', 'STUDENT', 'STUDIO', 'STYLE', 'SUGGESTIVE', 'SUPPORT', 'SWAY', 'SWIRL', 'SYMBOLIC', 'TALENT', 'TANGO', 'TARANTELLA', 'TEACHING', 'TECHNICAL', 'TECHNIQUE', 'TEMPOS', 'THEATER', 'THEATRICAL', 'THEMES', 'THERAPY', 'TIME', 'TIMING', 'TOUR', 'TOURING', 'TRADITIONAL', 'TRIBUTE', 'TROUPE', 'TUCK', 'TWIRL', 'TWIST', 'TYPE', 'UNITARDS', 'UPRIGHT', 'VARIETY', 'VISUAL', 'WALTZ', 'WHIMSY', 'WIELD', 'ZEAL'],
        "finance" : ['ACCOUNT', 'ACCOUNTING', 'ACCRUE', 'ACCUMULATE', 'ACQUISITION', 'ACTIVITY', 'ADJUSTABLE', 'ADJUSTMENT', 'AMEX', 'AMORTIZATION', 'ANNUAL', 'ANNUITY', 'APPRAISAL', 'ARBITRAGE', 'ARRANGEMENT', 'ARREARS', 'ASSETS', 'AUTHENTIC', 'AUTHORIZATION', 'AUTOMATED', 'AVERAGE', 'AVERAGING', 'BALANCE', 'BANK', 'BANKRUPT', 'BARTER', 'BEAR', 'BENEFICIARY', 'BID', 'BOND', 'BRACKET', 'BROKER', 'BROKERAGE', 'BULL', 'BUYING', 'BUYOUT', 'CALCULATION', 'CALL', 'CAPITAL GAIN', 'CARTEL', 'CASHIER', 'CERTIFICATE', 'CERTIFIED', 'CHART', 'CHURN', 'CIRCULATION', 'CLEARINGHOUSE', 'COLLATERAL', 'COLLECT', 'COMMISSION', 'COMMODITY', 'COMMON STOCK', 'COMPENSATION', 'COMPETITOR', 'COMPOUND', 'CONGLOMERATE', 'CONSOLIDATION', 'CONSORTIUM', 'CONSUMER', 'CONVERTIBLE', 'CORRECTION', 'COST', 'COUNTER', 'COUNTERSIGN', 'CREDIT', 'CURRENCY', 'CUSTODIAN', 'DEAL', 'DEBENTURE', 'DEBIT', 'DEBT', 'DEDUCTIBLE', 'DEDUCTION', 'DEFAULT', 'DELINQUENCY', 'DEMAND', 'DEPOSITORY', 'DEPRECIATION', 'DEPRESSION', 'DEREGULATION', 'DESIGNATION', 'DEVALUATION', 'DIFFERENTIAL', 'DISCOUNT', 'DISTRIBUTION', 'DIVERSIFY', 'DIVIDEND', 'DOWNTURN', 'DRAFT', 'DRIVEN', 'DUMP', 'EARN', 'ECONOMY', 'ELECTRONIC', 'ELIMINATION', 'EMBEZZLEMENT', 'ENDORSE', 'ENTERPRISE', 'ENTITY', 'EQUITY', 'ESCROW', 'ESTIMATION', 'EVALUATION', 'EXCEED', 'EXCHANGE RATE', 'EXORBITANT', 'EXPECTATION', 'EXTORTION', 'FAILURE', 'FALLING PRICE', 'FEDERAL', 'FEES', 'FIDUCIARY', 'FINANCE', 'FISCAL', 'FIXED', 'FLOAT', 'FORECLOSURE', 'FORFEITURE', 'FRUGALITY', 'FULFILLMENT', 'FUND', 'FUNDS', 'FUTURES', 'GAIN', 'GDP', 'GOLD', 'GOVERNMENT', 'GROWTH', 'GUARANTEE', 'GUARANTY', 'HIRING', 'IDENTIFICATION', 'ILLEGAL', 'IMPRINT', 'INCOME', 'INDEX', 'INDUSTRIAL', 'INFLATED PRICE', 'INSOLVENT', 'INSTALLMENT', 'INSTITUTION', 'INSUFFICIENT', 'INTANGIBLE', 'INTEREST', 'INTERMEDIARY', 'INTERVENTION', 'INVALIDATE', 'INVESTMENT', 'IRA', 'ISSUE', 'JOINT ACCOUNT', 'JUNK BOND', 'KEOGH PLAN', 'KITING', 'LAUNDERING', 'LENDING RATE', 'LEVERAGE', 'LIABILITY', 'LIEN', 'LIQUIDITY', 'LONG-TERM', 'LOW RISK', 'LUCRATIVE', 'MAINTAIN', 'MARGIN', 'MARKET', 'MATURITY', 'MEMBER', 'MERCANTILE', 'MERGER', 'MONEY', 'MONOPOLY', 'MUNICIPALS', 'MUTUAL FUNDS', 'NEGOTIABLE', 'NOTE', 'NYSE', 'OBLIGATION', 'ODD LOT', 'OPERATION', 'OPTION', 'OVERCOMPENSATE', 'OVERSIGHT', 'OWNERSHIP', 'PAR VALUE', 'PAYMENT', 'PEAKS', 'PERCENT', 'PLANNING', 'PLEDGE', 'POINTS', 'PORTFOLIO', 'PRACTICE', 'PREDETERMINE', 'PREFERRED STOCK', 'PREMIUM', 'PRINCIPAL', 'PRODUCT', 'PROFIT', 'PROGRESSIVE', 'PROMISSORY NOTE', 'PUBLIC', 'QUALITY', 'QUALM', 'QUANTITY', 'QUESTIONABLE', 'QUICK', 'QUITTANCE', 'QUOTE', 'RAID', 'RALLY', 'RAMIFICATION', 'RATE', 'RATIO', 'RECESSION', 'RECORD', 'RECOUP', 'RECOURSE', 'REDEMPTION', 'REDUCTION', 'REGULATION', 'REIMBURSE', 'RELIABILITY', 'RESERVES', 'RETIREMENT', 'RISK', 'RUMORS', 'SALE', 'SAVINGS', 'SECURITIES', 'SELECT', 'SELLING', 'SHARES', 'SHORT TERM', 'SHYLOCK', 'SLUMP', 'SOLVENCY', 'SPECULATE', 'SPECULATIVE', 'SPLIT', 'STAGFLATION', 'STOCK SPLIT', 'STOCKS', 'SUBSCRIPTION', 'SUMMARY', 'SURETY', 'SURPLUS', 'SURVIVORSHIP', 'SWAP', 'TAKEOVER', 'TAX SHELTER', 'TAX YEAR', 'TAXES', 'TECHNICAL', 'TENDER', 'THRIFTS', 'TICKER TAPE', 'TRADE', 'TRANSACTION', 'TRANSFER', 'TRANSFERABLE', 'TREASURY BILL', 'TRENDS', 'UNCOLLECTED', 'UNDERWRITER', 'UNIT', 'UNOFFICIAL', 'UNREGULATED', 'UNSECURED', 'UNTAXED', 'USURY', 'UTILITIES', 'VALUABLE', 'VALUE', 'VARIABLE', 'VAULT', 'VENTURE', 'VOID', 'VOUCHER', 'WAGE', 'WARRANT']
        }
topic = random.choice(topics)
word =  random.choice(words[topic])
word = word.replace(' ', '')
word = word.replace('-', '')
guessed = []
print(word)

# Game variables
hangman_img_status = 0

# Draw function


def draw():
    window.fill(WHITE)
    window.blit(images[hangman_img_status], (60, 60))

    # Topic
    t = word_fonts.render("Topic : " + topic.capitalize(), 1, YELLOWISH)
    window.blit(t, (400, 20))
    # Draw Buttons
    for letter in letters:
        x, y, ltr, clr = letter
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
        if win or hangman_img_status >= 6:
            end_game_loop(win)

# Reset the game


def reset():
    global guessed, word, title, hangman_img_status, letters
    guessed.clear()
    topic = random.choice(topics)
    word = random.choice(words[topic])
    word = word.replace(' ', '')
    word = word.replace('-', '')
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
    img_number = 0
    correct_word = word
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

        # Result text
        if win:
            text = RESULT_FONT.render("You won!!", 1, VIOLET)
        else:
            text = RESULT_FONT.render("You lost!!", 1, VIOLET)
            img_number = 6

        window.blit(images[img_number], (350, 25))
        window.blit(text, (320, 250))
        correct_text = word_fonts.render(correct_word, 1, PINK)
        window.blit(correct_text, (300, 385))
        # Play again button
        rect = pygame.draw.rect(window, RED, (350, 500, 220, 80))
        text = word_fonts.render("Play Again", 1, BLACK)

        # Check if Button is click or not
        m_x, m_y = pygame.mouse.get_pos()
        if rect.x + rect.width > m_x > rect.x and rect.y + rect.height > m_y > rect.y:
            text = word_fonts.render("Play Again", 1, WHITE)
            if click:
                reset()
                run = False
        window.blit(text, (rect.x + text.get_width() / 2 -
                           40, rect.y + text.get_height() / 2 - 5))

        pygame.display.flip()


if __name__ == "__main__":
    game_loop()
