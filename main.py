import pygame as pg
import sys
import pytmx
import pytmx.util_pygame

from Entities.TileMap import Tilemap

class Game:
    def __init__(self, window_size=(900,600)) -> None:
        pg.init()

        self.screen = pg.display.set_mode(window_size)
        self.clock = pg.time.Clock()
        self.tilemap = Tilemap('./Levels_Files/Level1.tmx')
        #self.map_image = self.tilemap.make_map()
        #self.map_rect = self.map_image.get_rect()
        self.tilemap_group = pg.sprite.Group()
        self.background_image_path = 'Assets/art/Treasure Hunters/Treasure Hunters/Palm Tree Island/Sprites/Background/BG Image.png'

    def draw_background_image(self):
        self.background_image = pg.image.load(self.background_image_path)
        self.background_image = pg.transform.scale(self.background_image, self.screen.get_size())
        
        self.screen.blit(self.background_image,(0,0))


    def load_map(self):
        self.tilemap.render(surface=self.screen, context=self)
    
    def draw_map(self):
        self.tilemap_group.update()
        self.tilemap_group.draw(self.screen)
        #self.screen.blit(self.map_image,(0,0))
    def exit(self):
        pg.quit()
        sys.exit(0)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.exit()
    
    def run(self):
        self.load_map()
        while True:
            #self.screen.fill((3, 63, 133))
            self.draw_background_image()
            
            self.check_events()

            self.draw_map()

            pg.display.update()
            
            self.clock.tick(60)
        
if __name__  == '__main__':
    game = Game()
    game.run()

            