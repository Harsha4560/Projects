import time
import random,os.path
import pygame,sys
from pygame.locals import *

pygame.font.init()


clock = pygame.time.Clock()
height = 900
width = 1300
canvas = pygame.display.set_mode((width, height))

pygame.display.set_caption('Brick Ball')

fullscreen = False

GRAY = (100, 100, 100)
NAVYBLUE = ( 60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = ( 0, 255, 255)

class Ball(pygame.sprite.Sprite):
    def __init__ (self, canvas, brick):
        super().__init__()
        self.x_speed = 10
        self.y_speed = -5
        self.score = 0
        self.pos = [brick.pos[0] , brick.pos[1] - 15]
        self.image = pygame.image.load('Ball.png').convert_alpha()
        self.rect = self.image.get_rect(
            center = self.pos
        )
    def vupdate(self):
        if self.rect[0] > width-50 or self.rect[0] < 0:
            self.x_speed = -1*self.x_speed
        if self.rect[1] < 0 or self.rect[1] > height-50:
            self.y_speed = -1 * self.y_speed
        
        if  self.rect.colliderect(brick.rect):
            self.y_speed = -1 * self.y_speed

        self.rect[0] += self.x_speed
        self.rect[1] += self.y_speed
    
class Blocks(pygame.sprite.Sprite):
    def __init__ (self, canvas, ball, posx, posy):
        super().__init__()
        self.canvas = canvas
        self.width = 100
        self.height = 50
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(
            center = [posx, posy]
        )
    
    def delet(self):
        if self.rect.colliderect(ball.rect):
            self.kill()
            ball.y_speed = -1 * ball.y_speed
            ball.score += 1

class Brick(pygame.sprite.Sprite):

    def __init__ (self, canvas):
        super().__init__()
        self.canvas = canvas
        self.x_speed = 20
        self.y_speed = 0
        self.height = 20
        self.width = 200
        self.pos = [width//2, height - 199]
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)
        self.rect = self.image.get_rect()



pygame.init()

run = True
brick = Brick(canvas)
ball = Ball(canvas, brick)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(brick)
all_sprites_list.add(ball)
all_blocks = pygame.sprite.Group()
for i in range(5):
    j = 0
    while j < width:
        block = Blocks(canvas, ball, j+50, i*100 + 25)
        all_blocks.add(block)
        all_sprites_list.add(block)
        j += 150

font = pygame.font.SysFont(None, 24)

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit()
            sys.exit()
    canvas.fill((0, 0, 0))
    pos = pygame.mouse.get_pos()
    brick.rect.x = pos[0]
    brick.rect.y = height - 150
    if ball.rect.y > height - 135:
        image = font.render('Score: '+str(ball.score), True, WHITE)
        canvas.blit(image, [width//2, height//2])
    else:
        ball.vupdate()
        for block in all_blocks:
            block.delet()
        all_sprites_list.draw(canvas)
        img = font.render('Score: '+str(ball.score), True, WHITE)
        canvas.blit(img, [10, height - 50])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()