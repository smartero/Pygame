'''
Mars Rover

A rover is a space exploration vehicle designed to move across the surface of a planet or other celestial body. Some rovers are partially or fully autonomous robots.

Rover Commands: 
MOV Moves the rover forward (F) or backward (B) by a specified number of steps. For example, the command "MOV F 3" moves the rover forward by 3 steps. 
TRN Turns the rover left (L) or right (R) by 15 degrees. For example, the command "TRN L" turns the rover left by 15 degrees. 
RCK Collects rocks for analysis. The rover has a container for the rocks with a limited space and can collect no more than five rocks. 
RLS Releases the last collected rock from the container. Executing this command five times makes the rover clean its container for rocks. 
ANL Performs a chemical analysis on the last collected rock. 
PIC Takes a picture of the area. The rover can save up to ten photos. 
LOG Prints the list of the commands executed recently. 

Create a program that visualizes the rover on the surface and provides an interface to type commands. Each typed command is then executed by the rover. 
'''

import sys
import pygame
import math
import io

# Initialize Pygame
pygame.init()

x, y = 200, 200
width, height = 51, 74
vel = 10
angle = 0
win_width, win_height = 900, 500

win = pygame.display.set_mode((win_width, win_height))
win.fill((0, 150, 0))
clock = pygame.time.Clock()
# Name of the game 
pygame.display.set_caption("Mars dron")

try:
    from urllib.request import urlopen
except ImportError:
    print("Sorry")
# Image URL
rover_url = 'https://i.ibb.co/Dzb0zht/rover.png'
rover_str = urlopen(rover_url).read()
# Create a file object (stream)
rover_file = io.BytesIO(rover_str)
# Load image from a file or stream
rover_s = pygame.image.load(rover_file)
# Remove background color from rover image
rover_s.set_colorkey((255, 255, 255))
rover_r = rover_s.get_rect(center = (x, y))
image = rover_s

font = pygame.font.Font(None, 20)
input_box = pygame.Rect(500, 0, 400, 500)
text = ''
text_rck = 'ROCKS: 0'
text_pic = 'PICTURES: 0'
text_anl = 'CHEMICAL ANALYSIS: 0'
log = []
log_text = ''

rck = 0 # rocks in rover (<= 5)
pic = 0 # taken pictures (<= 10)
log = [] # list of recent commands
anl = 0 # chemical analysis

def move_f(angle):
    x_0 = [0, 180, -180]
    y_0 = [90, 270, -90, -270]
    y = abs(n*vel*math.cos(angle))
    x = math.sqrt(math.pow(y,2) + math.pow(vel*n, 2))
    if angle in x_0:
        x = 0
        y = vel * n
    elif angle in y_0:
        x = vel * n
        y = 0
    return(x, y)

def turn(angle):
    global rover_r
    image = pygame.transform.rotate(rover_s, angle)
    rover_r = image.get_rect(center = (rover_r.center))
    return(image, rover_r)

run = True
while run:
    text_rck = 'RCK: {}'.format(rck)
    text_pic = 'PIC: {}'.format(pic)
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # number of steps to move and turn
                try:
                    n = int(''.join(i for i in text if i.isdigit()))
                except:
                    n = 1
                # Move forward
                if 'MOV F' in text:
                    if 0 <= angle < 90 or -360 < angle < -270:
                        x_side, y_side = move_f(angle)
                        rover_r.y -= y_side
                        rover_r.x -= x_side
                    if 90 <= angle < 180 or -270 <= angle < -180:
                        x_side, y_side = move_f(angle)
                        rover_r.y += y_side
                        rover_r.x -= x_side
                    if 180 <= angle < 270 or -180 <= angle < -90:
                        x_side, y_side = move_f(angle)
                        rover_r.y += y_side
                        rover_r.x += x_side
                    if 270 <= angle < 360 or -90 <= angle <= -15:
                        x_side, y_side = move_f(angle)
                        rover_r.y -= y_side
                        rover_r.x += x_side
                # Move backward
                if 'MOV B' in text:
                    if 0 <= angle < 90 or -360 <= angle < -270:
                        x_side, y_side = move_f(angle)
                        rover_r.y += y_side
                        rover_r.x += x_side
                    if 90 <= angle < 180 or -270 <= angle < -180:
                        x_side, y_side = move_f(angle)
                        rover_r.y -= y_side
                        rover_r.x += x_side
                    if 180 <= angle < 270 or -180 <= angle < -90:
                        x_side, y_side = move_f(angle)
                        rover_r.y -= y_side
                        rover_r.x -= x_side
                    if 270 <= angle < 360 or -90 <= angle < -15:
                        x_side, y_side = move_f(angle)
                        rover_r.y += y_side
                        rover_r.x -= x_side
                # Turn left
                if 'TRN L' in text:
                    angle += n*15 % 360
                    image, rover_r = turn(angle)
                # Turn right
                if 'TRN R' in text:
                    angle -= n*15 % 360
                    image, rover_r = turn(angle)
                # Collect rocks
                if 'RCK' in text:
                    if rck < 5:
                        rck += 1
                    else:
                        pass
                # Release rocks
                if 'RLS' in text:
                    if rck > 0:
                        rck -= 1
                    else:
                        rck = 0
                # Chemical analysis
                if 'ANL' in text:
                    anl += 1
                # Take picture
                if 'PIC' in text:
                    if pic == 10:
                        pass
                    else:
                        pic += 1
                # Print last 5 commands
                if 'LOG' in text:
                    log_text = '--'.join(log)
                if 'LOG' not in text:
                    log.append(text)
                else: 
                    pass
                if len(log) == 6:
                    log.pop(0)
                text = ''
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += (event.unicode).upper()

    clock.tick(30)
    # Render text
    txt_surf = font.render(text.upper(), True, (0, 180, 180))
    log_surf = font.render(log_text.upper(), True, (90, 180, 180))
    info = font.render('ROVER DATABASE', True, (90, 180, 180))
    info_rck_surf = font.render(text_rck.upper(), True, (90, 180, 180))
    info_pic_surf = font.render(text_pic.upper(), True, (90, 180, 180))
    info_anl_surf = font.render(text_anl.upper(), True, (90, 180, 180))
    
    win.fill((0, 0, 0), input_box)
        
    win.blit(txt_surf, (510, 10))
    win.blit(info, (510, 410))
    win.blit(log_surf, (510, 50))
    win.blit(info_rck_surf, (510, 430))
    win.blit(info_pic_surf, (510, 450))
    win.blit(info_anl_surf, (510, 470))
    win.blit(image, rover_r)
    pygame.display.update()

pygame.quit()
