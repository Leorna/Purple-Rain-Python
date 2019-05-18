import pygame
import sys
from random import randint as rand_int


class Drop:
    def __init__(self, screen):
        self.screen = screen
        self.x = rand_int(0, 600)
        self.y = -rand_int(0, 100)
        self.speed = rand_int(10, 20)
        self.len = rand_int(0, 75)
        
    def fall(self):
        self.y += self.speed
        if self.y > 600:
            self.y = -rand_int(0, 100)
            self.speed = rand_int(10, 20)
            
    def draw_drop(self):
        point_1 = (self.x, self.y)
        point_2 = (self.x, self.y + self.len)
        color = (255, 0, 255)
        pygame.draw.line(self.screen, color, point_1, point_2)
        
        
def rain():
    pygame.init()
    
    screen = pygame.display.set_mode((600, 600))
    
    drops = [Drop(screen)for i in range(200)]
    
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()
        
        screen.fill((0, 0, 0))
        
        for drop in drops:
            drop.fall()
            drop.draw_drop()
        
        pygame.display.flip()
        
        
rain()