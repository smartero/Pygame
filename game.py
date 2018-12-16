import sys
import pygame
pygame.init()

size = win_width, win_height = 500, 500
win = pygame.display.set_mode(size)
clock = pygame.time.Clock()
# Name of the game 
pygame.display.set_caption("Mars dron")
# Background
bg = pygame.image.load("moon.jpg")
# Sprite
rover_s = pygame.image.load("car.png").convert()
image = rover_s
pos = (200,200)
rect = image.get_rect().move(pos)
rect.center = pos
rover_s.set_colorkey((255, 255, 255))
rover_r = rover_s.get_rect(center = (200, 200))
x = 200
y = 200
width = 29
height = 29
vel = 5
angle = 0

# main loop
run = True
while run:
    # chech for events
    for event in pygame.event.get(): #list of the events that happen
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                flip = pygame.transform.flip(rover_s, False, True)
                rover_s = flip
            if event.key == pygame.K_r:
                image = pygame.transform.rotate(rover_s, angle)
                angle += 15 % 360
                i, j = rect.center
                rect = image.get_rect()
                rect.center = (i,j)
                #rover_r = rotate.get_rect(center=rover_r.center)
            if event.key == pygame.K_LEFT and rover_r.x > 5:
                rover_r.x -= vel 
                         
            
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT] and rover_r.x < win_width - 5 - width:
        rover_r.x += vel
    if keys[pygame.K_DOWN] and rover_r.y < win_height - 5 - height:
        rover_r.y += vel
    if keys[pygame.K_UP] and rover_r.y > 5:
        rover_r.y -= vel
    
    clock.tick(30)
    win.blit(bg, (0, 0))
    win.blit(rover_s, rover_r)
    win.blit(image, rect)  
    # refill the window with background picture
    pygame.display.update()
pygame.quit()