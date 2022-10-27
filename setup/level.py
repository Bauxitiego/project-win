import pygame
from settings import *

class Level:
    def __init__(self):
        #creates the surface for adding the texture 
        self.display_surface = pygame.display.get_surface()
        
        #sprite surfaces
        self.all_sprites = pygame.sprite.Group()
    
    
    def run(self,dt):
        self.display_surface.fill('grey')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update()