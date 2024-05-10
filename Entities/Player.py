import pygame as pg

from time import sleep
class Player(pg.sprite.Sprite):
    HORIZONTAL_ACCELERATION = 2
    HORIZONTAL_FRICTION = .2
    def __init__(self, position:pg.math.Vector2,size, group, context) -> None:
        super().__init__(group)
        self.size = size
        self.context = context
        self.position = position
        self.sprites = []
        self.speed = .2
        self.on_ground = False
        self.gravity = .5
        self.max_velocity = 3
        self.velocity = pg.math.Vector2(0,0)
        self.acceleration = pg.math.Vector2(0,self.gravity)
        
        self.on_ground = False
        self.is_jumping = False

        for i in range(1,2):
            image = pg.image.load(f'/home/luis/Downloads/free-pixel-art-tiny-hero-sprites/1 Pink_Monster/Pink_Monster.png')
            image = pg.transform.scale(image, self.size)
        
            self.sprites.append(image)

        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.position.x, self.position.y + self.size[1])
    
    def update(self):
        self.get_hits(self.context.tilemap_group)
        
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
       
        self.rect.topleft = [self.position[0], self.position[1]]
        self.velocity += self.acceleration * self.context.delta_time
        self.position += self.velocity
       
        self.acceleration = pg.math.Vector2(0,self.gravity)
        self.check_collison_y()
        self.check_collison_x()
        
        self.current_sprite += self.speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        else:
            self.image = self.sprites[int(self.current_sprite)]
            self.mask = pg.mask.from_surface(self.image)


    def check_collison_x(self):
        collisons = self.get_horizontal_hits(self.context.tilemap_group)
       
        #self.rect.bottom -=3
        if collisons:
            print(collisons)
            for tile in collisons:
                if self.velocity.x > 0:
                    
                    self.velocity.x = 0
                    self.position.x = tile.rect.left - self.rect.w
                    self.rect.x = self.position.x
                elif self.velocity.x < 0:
                    self.position.x = tile.rect.right
                    self.velocity.x = 0
                    self.rect.x = self.position.x

    def check_collison_y(self):
        self.on_ground = False
        
        collisons = self.get_hits(self.context.tilemap_group)
        for tile in collisons:
            if self.velocity.y > 0:
                self.on_ground = True
                self.is_jumping = False
                self.velocity.y = 0
                self.position.y = tile.rect.top
                self.rect.bottom  = self.position.y

    def get_horizontal_hits(self, tiles):
        hits = []
        for tile in tiles:
            if tile.type != 'Decoration':
                print(self.rect)
                if tile.rect.colliderect(self.rect):
                    self.rect.bottom -=1
                    if tile.rect.colliderect(self.rect):
                        pg.draw.rect(self.context.screen, 'red',pg.Rect(tile.position[0], tile.position[1],32,32,),1)
                        hits.append(tile)

        return hits

    
    def get_hits(self, tiles):
        hits = []
        for tile in tiles:
            if tile.type != 'Decoration':
                tilemask = pg.mask.from_surface(tile.image)
                offset = (tile.position[0] - self.position.x, tile.position[1] - self.position.y)

                overlap = self.mask.overlap(tilemask, offset)
                if overlap:
                
                    pg.draw.rect(self.context.screen, 'red',pg.Rect(tile.position[0], tile.position[1],32,32,),1)
                    hits.append(tile)
            
        return hits
 
