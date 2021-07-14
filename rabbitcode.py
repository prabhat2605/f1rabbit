import pygame
import random
import time

pygame.init()


#creating display
screen = pygame.display.set_mode((900, 600))
intro_screen = pygame.image.load('C:\\Users\\Dell_NB\\PycharmProjects\\pygame tutorial\\background-clipart-landscape.jpg')
rabbit_image = pygame.image.load('C:\\Users\\Dell_NB\\PycharmProjects\\pygame tutorial\\rabit_image-removebg-preview (1).png')
food_image =pygame.image.load('C:\\Users\\Dell_NB\\PycharmProjects\\pygame tutorial\\carrot_image_2-removebg-preview.png')
#giving title for game
pygame.display.set_caption("F1 Rabbit")



#creating intro window







font =pygame.font.SysFont('None', 55)
def score_view(text, color, x, y):
    screen_1 = font.render(text, True, color)
    screen.blit(screen_1,[x,y] )
def text_screen(text, color, x, y):
    screen_2 =font.render(text, True,  color)
    screen.blit(screen_2, [x,y])
#pygame.mixer.music.load("C:\\Users\\Dell_NB\\PycharmProjects\\pygame tutorial\\Dj Waley Babu-(Mr-Jatt.com).mp3")
#pygame.mixer.music.play()

exit_game = False

def gameloop():
    exit_game = False
    black = (0, 0, 0)
    red = (255, 0, 0)
    white = (255, 255, 255)
    X = 60
    Y = 90
    snake_size = 25
    snake_size_x = 25
    snake_size_y = 25
    init_velocity = 5
    fps = 30
    clock = pygame.time.Clock()
    turn = True
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(60,450)
    food_y = random.randint(60, 450)
    score = 0

    with open("C:\\Users\\Dell_NB\\.PyCharmCE2018.3\\config\\scratches\\hiscore.txt","r") as f:
        hiscore = f.read()

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if  event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =  init_velocity
                        velocity_y = 0
                    if event.key  == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key  == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -init_velocity
                    if event.key  == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = +init_velocity
        screen.fill((255, 255, 255))
        screen.blit(intro_screen,(0,0))



        X = X + velocity_x
        Y    = Y + velocity_y

        if (X < 0 or X > 900) or (Y < 0 or Y > 600):
            with open("C:\\Users\\Dell_NB\\.PyCharmCE2018.3\\config\\scratches\\hiscore.txt", "w") as f:
                f.write(str(hiscore))
            break


        if abs(food_x - X)< 20 and abs(food_y - Y)<20:
            food_x = random.randint(10, 450)
            food_y = random.randint(10, 450)
            if init_velocity < 100:
             init_velocity +=1
            score += 10
        if score > int(hiscore):
            hiscore = score


        score_view(str(f"score:{score}    hiscore:{str(hiscore)}"), white ,50,50 )
        screen.blit(food_image,(food_x, food_y))
        pygame.draw.rect(screen, black,[0, 0, 10, 600])
        pygame.draw.rect(screen, black, [1, 0, 900, 10])
        pygame.draw.rect(screen, black, [890, 0, 10, 600])
        pygame.draw.rect(screen, black, [1, 590, 900, 10])
        #pygame.draw.rect(screen, black, [X, Y, snake_size_x, snake_size_y])
        screen.blit(rabbit_image, (X, Y))
        pygame.display.update()
        clock.tick(fps)

screen_2 = pygame.display.set_mode((900, 600))
first_window = pygame.image.load("C:\\Users\\Dell_NB\\PycharmProjects\\pygame tutorial\\360_F_191348533_MkI9rXho6D7ajkuRuvHYZA0DncbEAHJN.jpg")
screen_2.blit(first_window, (0,0))
pygame.display.update()
time.sleep(5)


gameloop()


while not exit_game:

    screen.fill((0,0,0))
    text_screen('GAME OVER PRESS'
                ' ENTER TO PLAY AGAIN', (255,0,0),45, 300)
    pygame.display.update()



    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                gameloop()
