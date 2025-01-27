import pytmx
import pygame as pg
from Entities.Tile import Tile
from Entities.Decoration.BackRegularPalmTree import BackRegularPalmTree
class Tilemap:
    def __init__(self, filename) -> None:
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height* tm.tileheight
        self.tmx_data = tm 

    
    def render(self, surface,context):
        

        
        for object in self.tmx_data.objects:
            if object:
                
                position = {'x':object.x, 'y':object.y}
                
                palmtree = BackRegularPalmTree(position=position, size=(64+5,64+5), group=context.tilemap_group)
                context.tilemap_group.add(palmtree)
        for layer in self.tmx_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x,y, gid in layer:
                    image = self.tmx_data.get_tile_image_by_gid(gid)
                    atributts = self.tmx_data.get_tile_properties_by_gid(gid)

                    position = (x*self.tmx_data.tilewidth, y*self.tmx_data.tileheight)
                    collider = None 
                    if atributts:
                        collider = atributts['colliders']

                    if image and collider:
                        #surface.blit(tile, position)
                        tile = Tile(position=position, surface=image,group=context.tilemap_group)
                        context.tilemap_group.add(tile)
        
            
    def make_map(self):
        temp_surface =  pg.Surface((self.width, self.height))
        self.render(temp_surface)

        return temp_surface