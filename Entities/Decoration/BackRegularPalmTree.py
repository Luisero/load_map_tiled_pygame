import pygame as pg


class BackRegularPalmTree(pg.sprite.Sprite):
    def __init__(self, position,size, group) -> None:
        super().__init__(group)
        self.size = size
        self.position = position
        self.sprites = []
        self.speed = .1
        self.type = 'Decoration'

        for i in range(1,5):
            image = pg.image.load(f'./Assets/art/Treasure Hunters/Treasure Hunters/Palm Tree Island/Sprites/Back Palm Trees/Back Palm Tree Regular 0{i}.png')
            image = pg.transform.scale(image, self.size)
            self.sprites.append(image)

        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.position['x'], self.position['y']]
    
    def update(self, camera_scroll):
        self.current_sprite += self.speed

        position = {'x':self.position['x']+camera_scroll[0], 'y':self.position['y']+ camera_scroll[1]}
        self.position = position
        self.rect.topleft =  [self.position['x'], self.position['y']]
        
        

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        else:
            self.image = self.sprites[int(self.current_sprite)]
