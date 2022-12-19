import time
import random
import pygame

word_list = [
    'python', 'goal', 'software', 'engineer', 'coding', 'business', 'world', 'product'
]

pygame.init()

#create game window
window = pygame.display.set_mode((800,600))

#loading background image
bg = pygame.image.load('bg_img.jpg')

bg = pygame.transform.scale(bg, (800,600))

my_font = pygame.font.SysFont('Segoe UI', 35)

speed = 0.6
score = 0
game_not_over = True
game_started = False

def generate_word():
    global curr_word, player_word, x , y, speed

    #choosing random X co-ordinate for current word
    x = random.randint(150, 550)
    # Y co-ordinate
    y = 150

    #increase speed
    speed = speed + 0.05

    player_word = ''

    curr_word = random.choice(word_list)


generate_word()


def put_text(x, y, text, sz):
    my_font = pygame.font.SysFont('Segoe UI', sz)

    my_text = my_font.render(text, True, (0,0,0))

    window.blit(my_text, (x,y))


def display_screen():
    #blitting background image
    window.blit(bg, (0,0))

    #if game od over
    if game_not_over is False:
        put_text(200, 200, "Game over!", 100)
        put_text(200, 300, "Score" + str(score), 50)

    else:
        put_text(200, 200, "Press a key to start playing!", 50)

    pygame.display.flip()

    #remain true until key is pressed
    wait = True
    while wait:
        for e in pygame.event.get():
            #user quits window
            if e.type == pygame.QUIT:
                pygame.quit()

            #any other key pressed 
            if e.type == pygame.KEYDOWN:
                wait = False
