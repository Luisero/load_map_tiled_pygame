import pygame as pg
import sys
import pytmx
import pytmx.util_pygame
from Entities.Player import Player

from Entities.TileMap import Tilemap

class Game:
    def __init__(self, window_size=(900,600)) -> None:
        pg.init()
        pg.font.init()
        self.font = pg.font.SysFont(None, 36)
        self.collide_text = ''
        self.screen = pg.display.set_mode(window_size)
        self.clock = pg.time.Clock()
        self.tilemap = Tilemap('./Levels_Files/Level1.tmx')
        #self.map_image = self.tilemap.make_map()
        #self.map_rect = self.map_image.get_rect()
        self.tilemap_group = pg.sprite.Group()
        self.entities_group = pg.sprite.Group()
        self.player = Player(group=self.entities_group, position=pg.math.Vector2(30,350), size=(32*1.5,32*1.5), context=self)
        self.entities_group.add(self.player)
        self.background_image_path = 'Assets/art/Treasure Hunters/Treasure Hunters/Palm Tree Island/Sprites/Background/BG Image.png'
        self.camera_scroll = [0,0]
        self.delta_time = 0
        self.TARGET_FPS = 60

        self.gravity = 1
        

    def draw_background_image(self):
        self.background_image = pg.image.load(self.background_image_path)
        self.background_image = pg.transform.scale(self.background_image, self.screen.get_size())
        
        self.screen.blit(self.background_image,(0,0))


    def load_map(self):
        self.tilemap.render(surface=self.screen, context=self)
    
    def draw_map(self):
        self.tilemap_group.update(self.camera_scroll)
        self.tilemap_group.draw(self.screen)
        #self.screen.blit(self.map_image,(0,0))
    def exit(self):
        pg.quit()
        sys.exit(0)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.exit()
            
        self.camera_scroll = [00,0]

        
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.player.acceleration.x = -Player.HORIZONTAL_ACCELERATION
            if self.player.position.x < 60:
                self.camera_scroll[0] = 5
                self.player.acceleration.x =Player.HORIZONTAL_ACCELERATION
            #self.camera_scroll[0] = 1
        elif keys[pg.K_d]:
            #self.camera_scroll[0] = -1
            self.player.acceleration.x = Player.HORIZONTAL_ACCELERATION
            if self.player.position.x > self.screen.get_width() - self.player.size[0]*3:
                self.camera_scroll[0] = -5
                self.player.acceleration.x= -Player.HORIZONTAL_ACCELERATION

        elif keys[pg.K_SPACE]:
            self.player.acceleration.y = -1
        
        
        
        
    
    def run(self):
        self.load_map()
        while True:
            self.delta_time = self.clock.tick(self.TARGET_FPS) *.001 * self.TARGET_FPS
            #self.screen.fill((3, 63, 133))
            self.draw_background_image()
            
            self.check_events()

            self.draw_map()

            self.entities_group.update()
            self.entities_group.draw(self.screen)
            self.collide_text = f'FPS: {str(self.clock.get_fps())[:2]}'
            self.collide_text_render = self.font.render(self.collide_text, True, 'white')
            self.screen.blit(self.collide_text_render, (10, 35))
            pg.display.update()
            
            self.clock.tick(60)
        
if __name__  == '__main__':
    game = Game()
    game.run()

            