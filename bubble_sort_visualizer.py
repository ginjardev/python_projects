import pygame

#initialise pygame window
pygame.init()
array1 = ""
array = []

# screen dimensions
screen = pygame.display.set_mode(700, 500)
font = pygame.font.SysFont('ubuntu mono', 20)
run = True


def show_text(array):
    screen.fill((0, 0, 150, 0))
    block = font.render(str(array), True, (255, 255, 150))
    screen.blit(block, (20,20))


def draw_rect():
    for i in range(len(array)):
        pygame.draw.rect(screen, (255, 125,0), ((50+i*25,50, 20, array[i]*2)))
    pygame.display.update()


def bubble_sort():
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j +1]:
                array[j], array[j+1] = array[j+1], array[j]
        
        array1 = [str(i) for i in array]
        array1 = ",".join(array1)
        show_text(array1)
        draw_rect()
        pygame.time.delay(500)
        pygame.display.update()

    
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                array = array1.split(",")
                array = [int(i) for i in array]
                draw_rect()
                pygame.time.delay(3000)
                bubble_sort()
            elif event.key == pygame.K_BACKSPACE:
                array1 = array1[:-1]
            else:
                array1 += event.unicode
                show_text(array1)
                pygame.display.update()
        elif event.type == pygame.QUIT:
            run = False

pygame.quit()


screen.fill((0,0,0,0))
block = font.render("Bubble Sort Visualization")
screen.blit(block, (0,20))
block1 = font.render("Enter input and press ENTER to visualize", True, (255,255,150))
screen.blit(block1, (0,40))
block2 = font.render("Add comma to separate the integers and backspace to pop", True, (255,255,150))
screen.blit(block2, (0,60))
pygame.display.update()