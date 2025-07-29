import math
import random
import pygame


#display setup
pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game')

# button var
RADIUS = 20
RAD = 30
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i//13) * (GAP + RADIUS * 2 ))
    letters.append([x, y, chr(A + i), True])

# font
LETTER_FONT = pygame.font.SysFont('Comic Sans MS', 20)
TITTLE_FONT = pygame.font.SysFont('commicsans', 70)
# images
images = []
for i in range(7):
    image = pygame.image.load('hangman'+ str(i) +'.png')
    images.append(image)

# game var
hangman_status = 0

words = ["SAME", "TRANQUIL", "TENT", "USE", "HOT", "THREAD", "MANY", "DEAFENING", "BEAR", "TRIP", "MOUNTAIN", "TEACHING", "CROSS", "SEIZE", "COLORFUL", "ELBOW", "GLANCE","GUIDE", "CANCEL", "GLUE", "BALANCE", "SENTENCE", "LIFT", "SECRETION", "WEALTH", "AUNT", "NETWORK", "HILL", "IMPACT", "MENU"]

word = random.choice(words)

guessed = []

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#game loop: not used at the moment
#FPS = 60
#clock = pygame.time.Clock()
running = True


def draw():
    screen.fill(WHITE)

    # draw tittle
    text = TITTLE_FONT.render('Hangman', True, BLACK)
    screen.blit(text, (WIDTH/2 - text.get_width()/2, 20))


    # draw word
    display_word = ''
    for letter in word:
        if letter in guessed:
            display_word += letter + ''
        else:
            display_word += '_ '
    text = LETTER_FONT.render(display_word, True, BLACK)
    screen.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(screen, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, True, BLACK)
            screen.blit(text, (x - text.get_width()/2, y-text.get_height()/2))

    screen.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    screen.fill(WHITE)
    text = LETTER_FONT.render(message, True, BLACK)
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


# end screen
def ending():
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            g_x, g_y = pygame.mouse.get_pos()
            print(g_x, g_y)
            if 326 < g_x < 476 and 226 < g_y < 255:
                main()


    ending_text = TITTLE_FONT.render('PLAY AGAIN?', True, WHITE)
    screen.blit(ending_text, (WIDTH / 2 - ending_text.get_width() / 2, 20))




    ending_yes = LETTER_FONT.render('YES', True, BLACK)
    ending_no = LETTER_FONT.render('NO', True, BLACK)
    pygame.draw.rect(screen, WHITE, (350 - ending_yes.get_width() / 2, 240 - ending_yes.get_height() / 2, 150, 30))
    pygame.draw.rect(screen, WHITE, (350 - ending_no.get_width() / 2, 340 - ending_no.get_height() / 2, 150, 30))
    tgt = LETTER_FONT.render('YES', True, BLACK)

    screen.blit( ending_yes, (400 - ending_yes.get_width()/2, 240 - ending_yes.get_height()/2))
    screen.blit(ending_no, (400 - ending_yes.get_width() / 2, 340 - ending_yes.get_height() / 2))
    pygame.display.update()



# main menu
def main_menu():
    screen.fill(WHITE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                g_x, g_y = pygame.mouse.get_pos()
                print(g_x, g_y)
                if 326 < g_x < 476 and 226 < g_y < 255:
                    main()
                elif 326 < g_x < 476 and 326 < g_y < 355:
                    options_menu()
                elif 326 < g_x < 476 and 426 < g_y < 455:
                    pygame.quit()



        menu_text =  pygame.font.SysFont('Comic Sans MS', 100)

        MAIN_MENU = menu_text.render('MAIN MENU', True, BLACK)
        OPTIONS_BUTTON = LETTER_FONT.render('OPTIONS', True, WHITE)
        QUIT_BUTTON = LETTER_FONT.render('QUIT', True, WHITE)
        PLAY_BUTTON = LETTER_FONT.render('PLAY', True, WHITE)

        # DRAWING BUTTONS
        pygame.draw.rect(screen, BLACK, (350 - PLAY_BUTTON.get_width() / 2, 240 - PLAY_BUTTON.get_height() / 2, 150, 30))
        pygame.draw.rect(screen, BLACK, (350 - PLAY_BUTTON.get_width() / 2, 340 - OPTIONS_BUTTON.get_height() / 2, 150, 30))
        pygame.draw.rect(screen, BLACK, (350 - PLAY_BUTTON.get_width() / 2, 440 - OPTIONS_BUTTON.get_height() / 2, 150, 30))


        screen.blit( PLAY_BUTTON, (400 - PLAY_BUTTON.get_width()/2, 240 - PLAY_BUTTON.get_height()/2))
        screen.blit( OPTIONS_BUTTON, (400 - OPTIONS_BUTTON.get_width()/2, 340 - OPTIONS_BUTTON.get_height()/2))
        screen.blit(QUIT_BUTTON, (400 - QUIT_BUTTON.get_width() / 2, 440 - QUIT_BUTTON.get_height() / 2))

        # DRAW MAIN MENU
        screen.blit(MAIN_MENU, (WIDTH / 2 - MAIN_MENU.get_width() / 2, 20))

        # testing DRAWING BUTTONS
        #pygame.draw.rect(screen, BLACK, (350 - PLAY_BUTTON.get_width()/2, 240 - PLAY_BUTTON.get_height()/2, 100, 30))
        #pygame.draw.circle(screen, BLACK, (400, 340), RAD, 5)
        #pygame.draw.circle(screen, BLACK, (400, 440), RAD, 5)

        pygame.display.update()
        # testing mouse collison
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #g_x, g_y = pygame.mouse.get_pos()
            #print(g_x, g_y)
            #if 326 < g_x < 476 and 226 < g_y < 255:
                #main()
            #elif 326 < g_x < 476 and 326 < g_y < 355:
                #screen.fill(BLACK)
            #elif 326 < g_x < 476 and 426 < g_y < 455:
                #pygame.quit()

def options_menu():
    screen.fill(WHITE)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                g_x, g_y = pygame.mouse.get_pos()
                print(g_x, g_y)
                if 326 < g_x < 476 and 226 < g_y < 255:
                    mainveryhard()
                elif 326 < g_x < 476 and 326 < g_y < 355:
                    mainhard()
                elif 326 < g_x < 476 and 426 < g_y < 455:
                    main()

        menu_text = pygame.font.SysFont('Comic Sans MS', 100)

        MAIN_MENU = menu_text.render('DIFFICULTY', True, BLACK)
        OPTIONS_BUTTON = LETTER_FONT.render('HARD', True, WHITE)
        QUIT_BUTTON = LETTER_FONT.render('NORMAL', True, WHITE)
        PLAY_BUTTON = LETTER_FONT.render('VERY HARD', True, WHITE)

        # DRAWING BUTTONS
        pygame.draw.rect(screen, BLACK,
                         (350 - PLAY_BUTTON.get_width() / 2, 240 - PLAY_BUTTON.get_height() / 2, 200, 30))
        pygame.draw.rect(screen, BLACK,
                         (350 - PLAY_BUTTON.get_width() / 2, 340 - OPTIONS_BUTTON.get_height() / 2, 200, 30))
        pygame.draw.rect(screen, BLACK,
                         (350 - PLAY_BUTTON.get_width() / 2, 440 - OPTIONS_BUTTON.get_height() / 2, 200, 30))

        screen.blit(PLAY_BUTTON, (400 - PLAY_BUTTON.get_width() / 2, 240 - PLAY_BUTTON.get_height() / 2))
        screen.blit(OPTIONS_BUTTON, (400 - OPTIONS_BUTTON.get_width() / 2, 340 - OPTIONS_BUTTON.get_height() / 2))
        screen.blit(QUIT_BUTTON, (400 - QUIT_BUTTON.get_width() / 2, 440 - QUIT_BUTTON.get_height() / 2))

        # DRAW MAIN MENU
        screen.blit(MAIN_MENU, (WIDTH / 2 - MAIN_MENU.get_width() / 2, 20))



        pygame.display.update()



# core game loops/difficulty

def mainhard():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                M_x, M_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    distance = math.sqrt((M_x - x) ** 2 + (M_y - y) ** 2)
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("YOU WON!")
            pygame.quit()

        if hangman_status == 4:
            display_message("GAME OVER")
            pygame.quit()
            #ending()


def mainveryhard():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                M_x, M_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    distance = math.sqrt((M_x - x) ** 2 + (M_y - y) ** 2)
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("YOU WON!")
            pygame.quit()

        if hangman_status == 2:
            display_message("GAME OVER")
            pygame.quit()
            #ending()


def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                M_x, M_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    distance = math.sqrt((M_x - x) ** 2 + (M_y - y) ** 2)
                    if distance < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("YOU WON!")
            pygame.quit()

        if hangman_status == 6:
            display_message("GAME OVER")
            pygame.quit()
            #ending()




while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            main_menu()


#final quit; pygame.quit()


