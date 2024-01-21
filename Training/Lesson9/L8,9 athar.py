import arcade

tileSize =  18
WidthMap = 30 * tileSize
HeightMap = 20 * tileSize
title = "Map 1 -- Journey 1"
MovementSpeed = 2
JumpSpeed = 6
ZoomFactor = 0.5  # 50% zoom-out


class myMaps(arcade.Window):
    def __init__(self):
        super().__init__(WidthMap,HeightMap,title)

        self.bg = None
        self.ground = None
        self.obstacle = None
        self.item = None
        self.item2 = None
        self.item3 = None
        self.player = None
        self.coin = None

        self.Map1 = None
        self.physics_engine = None
        self.left_pressed = None
        self.right_pressed = None



    def setup(self):
        #LOad the map into the program
        self.Map1 = arcade.load_tilemap("mapku9.json",1)
        print("Available sprite lists:", self.Map1.sprite_lists.keys())
        #load all the map layers into the initialized obj
        self.bg = self.Map1.sprite_lists["bgg"]
        self.ground = self.Map1.sprite_lists["ground"]
        #self.obstacle = self.Map1.sprite_lists["obstacle"]
        self.item = self.Map1.sprite_lists["decor-back"]
        self.item2 = self.Map1.sprite_lists["decor-more"]
        self.item3 = self.Map1.sprite_lists["decor-up"]
        self.coin = self.Map1.sprite_lists["COIN"]



        self.player = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk5.png", 0.2)
        self.player.center_x = 4 * tileSize
        self.player.center_y = 13 * tileSize

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.ground)



    def on_draw(self):
        arcade.start_render()


        self.bg.draw()
        self.item.draw()
        self.ground.draw()
        self.item2.draw()
        self.item3.draw()
        self.coin.draw()
        self.player.draw()

    def on_key_press(self, key, modifiers: int):

        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = JumpSpeed

    def on_key_press(self, key, modifiers: int):

        if key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = JumpSpeed

    def on_update(self, delta_time: float):
        self.physics_engine.update()

        if self.left_pressed == True and not self.right_pressed == True:
            self.player.change_x = -MovementSpeed
        elif self.right_pressed == True and not self.left_pressed == True:
            self.player.change_x = MovementSpeed
        else:
            self.player.change_x = 0



map1 = myMaps()
map1.setup()
arcade.run()