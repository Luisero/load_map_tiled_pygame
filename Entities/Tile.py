import pygame as pg


class Tile(pg.sprite.Sprite):
    def __init__(self,position, surface, group) -> None:
        super().__init__(group)
        self.image = surface
        self.position = position
        self.rect = self.image.get_rect(topleft = position)