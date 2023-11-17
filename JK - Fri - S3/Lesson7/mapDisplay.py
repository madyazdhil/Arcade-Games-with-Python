import arcade

pixelTileSize = 70
ScrWid = 15 * pixelTileSize
ScrHig = 10 * pixelTileSize

class MyMaps(arcade.Window):
    def __init__(self):
        super().__init__(ScrWid, ScrHig, "Map 1 -- Journey 1")
        self.bg = None
        self.ground = None
        self.item = None
        self.player = None

        self.tileMap = None

    def setup(self):
        #setup to load the tile map into the program

        self.tileMap = arcade.load_tilemap("map1.json",1)
        self.bg = self.tileMap.sprite_lists["background"]
        self.ground = self.tileMap.sprite_lists["ground"]
        self.item = self.tileMap.sprite_lists["items"]

    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        self.ground.draw()
        self.item.draw()


arena1 = MyMaps()
arena1.setup()
arcade.run()