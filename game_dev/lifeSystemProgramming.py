## Simulate life processes.

import pygame, random
pygame.init()

## Color Palette = (R, G, B) values
aqua = (0,255,255)
navy = (0,0,205)
black = (0,0,0)
skin = (255,228,196)
orange = (255,97,3)
metallic = (198,226,255)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
## End Palette

screen = pygame.display.set_mode([500, 500]) ## Resolution
pygame.display.set_caption('Not Adventure Capitalist') ## Title of the game
background = black  ## Variable that can be edited later
frameRate = 60  ## Framerate 
font = pygame.font.Font('freesansbold.ttf', 16) ## Font
timer = pygame.time.Clock() ## Help run our game at 60 FPS

class Particle():
    def __init__(self, color):
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)
        self.col = color
        self.dx = 0
        self.dy = 0
    
        
def create(number, color):
    particles = []
    for i in range(0, number):
        col = random.randint(0, 100)%len(color)
        particles.append(Particle(color[col]))

    return particles
