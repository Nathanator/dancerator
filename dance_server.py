__author__ = 'nathan'

import socket
import pygame, sys
from pygame.locals import *

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

valid_messages = ['up',
                  'down',
                  'left',
                  'right']

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

# set us up the window
DISPLAYSURF = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255,255,255)
catImg = pygame.image.load('cat.png')
catx = 400
caty = 300
direction = 'right'


while True:
    direction, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", direction

    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    direction = ''

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)