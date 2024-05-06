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
        self.gravity = 1
        self.max_velocity = 3
        self.velocity = pg.math.Vector2(0,5)
        self.acceleration = pg.math.Vector2(0,0)

        for i in range(1,6):
            image = pg.image.load(f'./Assets/art/Treasure Hunters/Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose with Sword/09-Idle Sword/Idle Sword 0{i}.png')
            image = pg.transform.scale(image, self.size)
        
            self.sprites.append(image)

        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.position.x, self.position.y + self.size[1])
    
    def update(self):
        
        self.velocity.y = 5
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
        
        self.check_collision_x()
        self.check_collision_y()
        
        self.rect.topleft = [self.position[0], self.position[1]]
        self.velocity += self.acceleration
        self.position += self.velocity
       
        self.gravity = 0
        self.acceleration = pg.math.Vector2(0,self.gravity)
        
        self.current_sprite += self.speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        else:
            self.image = self.sprites[int(self.current_sprite)]
            self.mask = pg.mask.from_surface(self.image)


    
    def get_hits(self, tiles):
        hits = []
        for tile in tiles:
            if tile.type != 'Decoration':
                tilemask = pg.mask.from_surface(tile.image)
                offset = (tile.position[0] - self.position.x, tile.position[1] - self.position.y)

                overlap = self.mask.overlap(tilemask, offset)
                if overlap:
                    hits.append(tile)
            
        return hits
    
    def check_collision_x(self):
        collisions  = self.get_hits(self.context.tilemap_group)
        
       
        for tile in collisions:
            if self.velocity.x > 0:
                if not self.on_ground:
                    self.position.x = tile.rect.left - self.rect.w
                self.velocity.x = 0
                self.acceleration.x = 0
                
            elif self.velocity.x <0:
                if not self.on_ground:
                    self.position.x = tile.rect.right
                self.rect.x = self.position.x
                self.velocity.x = 0
                self.acceleration.x = 0

    def check_collision_y(self):
        self.on_ground = False 
        
       
        collisions  = self.get_hits(self.context.tilemap_group)
       
        for tile in collisions:
            if self.velocity.y > 0:
                self.on_ground = True 
                print(self.on_ground)
                self.is_jumping = False 
                self.velocity.y =0
                self.gravity *=-1
                
                print(f'Bottom: {self.rect.bottom}')
                print(f'Tile top : {self.position.y}')
                print(self.position)
                self.rect = self.image.get_rect()
                #self.rect.bottom = tile.rect.top - self.mask.get_size()[1]
                #  self.position.y = self.rect.bottom
                
                
                
                print(self.rect)
    
            
            

    
    
