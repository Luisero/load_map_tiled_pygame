import pygame as pg
import math

class Tile(pg.sprite.Sprite):
    def __init__(self,position, surface, group) -> None:
        super().__init__(group)
        self.image = surface
        #self.original_position = [position[0], position[1]]
        #self.position = [position[0], position[1]+200]
        self.position = position
        self.type = 'Tile'
        
        
        self.rect = self.image.get_rect(topleft =self.position)
        self.camera_scroll_vel = [0,0]

        
        #self.animation_velocity = 2
        #self.animation_acceleration = .2

    def update(self, camera_scroll):
       
        position = (self.position[0]+camera_scroll[0], self.position[1]+ camera_scroll[1])
        self.position = position
        self.rect = self.image.get_rect(topleft =self.position)
'''
    def update(self):
        self.animation_velocity += self.animation_acceleration
        if self.position[1] > self.original_position[1]:
            self.position[1] -= self.animation_velocity
        self.rect = self.image.get_rect(topleft = (self.position[0],int(self.position[1])))
'''
