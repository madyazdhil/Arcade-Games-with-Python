import arcade

tileSize = 70
WidthMap = 15 * tileSize
HeightMap = 10 * tileSize
title = "Map 1 -- Journey 1"
class myMaps(arcade.Window):
    def __init__(self):
        super().__init__(WidthMap,HeightMap,title)

        self.bg = None
        self.ground = None
        self.obstacle = None
        self.item = None

        self.Map1 = None

    def setup(self):
        #LOad the map into the program
        self.Map1 = arcade.load_tilemap("map1.json",1)

        #load all the map layers into the initialized obj
        self.bg = self.Map1.sprite_lists["bg"]
        self.ground = self.Map1.sprite_lists["ground"]
        self.obstacle = self.Map1.sprite_lists["obstacle"]
        self.item = self.Map1.sprite_lists["items"]

    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        self.ground.draw()
        self.item.draw()
        self.obstacle.draw()


map1 = myMaps()
map1.setup()
arcade.run()