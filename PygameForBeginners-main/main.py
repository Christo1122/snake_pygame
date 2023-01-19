import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("first game")

WHITE = (255,255,255)
BLACK =  (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2, 0 ,10 ,HEIGHT)

FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VEL = 5
BULLET_VELOCITY = 7

YELLOW_SPACESHIP_IMAGE =  pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')), -90)
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)) #SCALE
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'spaceship_red.png')),90)
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE,( SPACESHIP_WIDTH, SPACESHIP_HEIGHT))



def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update() 

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
            yellow.x -= VEL
    if keys_pressed[pygame.K_d]and yellow.x + VEL + yellow.width - BORDER.x < 0: #left
            yellow.x += VEL  
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0 : #left
            yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT: #left
            yellow.y += VEL   

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x + VEL > BORDER.x + BORDER.width: #left
            red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #left
            red.x += VEL  
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #left
            red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT: #left
            red.y += VEL               

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    bullet = []  
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) #make sure it is 60fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_LCTRL:
                        bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2)
                        yellow_bullets.append

                if event.type == pygame.K_RCTRL:
                        bullet = pygame.Rect(red.x + red.width, red.y + red.height/2)
                        red_bullets.append


        keys_pressed = pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed, yellow)     
        red_handle_movement(keys_pressed, red)          
        draw_window(red, yellow )
    pygame.quit()

if __name__ == "__main__":
    main()   #so the game wont run if this file is imported
