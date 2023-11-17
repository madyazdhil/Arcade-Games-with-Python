import arcade

Tile_size = 70

WidthScreen = 15 * Tile_size
HeightScreen = 10 * Tile_size
title = "Map 1 -- Journey 1"

class MyMap(arcade.Window):
    def __init__(self):
        super().__init__(WidthScreen,HeightScreen,title)

        self.bg = None #background
        self.platform = None #ground
        self.deco = None #decoration
        self.harm = None #obstacle
        self.map1 = None

    def setup(self):

        #load map
        self.map1 = arcade.load_tilemap("map1.json")

        #load all the layers into the attributes
        self.bg = self.map1.sprite_lists["backround"]
        self.platform = self.map1.sprite_lists["ground"]
        self.deco = self.map1.sprite_lists["decoration"]
        self.harm = self.map1.sprite_lists["obstacle"]

    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        self.deco.draw()
        self.harm.draw()
        self.platform.draw()

map1 = MyMap()
map1.setup()
arcade.run()

