import arcade

tileSize =  18
WidthMap = 30 * tileSize
HeightMap = 20 * tileSize
title = "Map 1 -- Journey 1"
MovementSpeed = 2
JumpSpeed = 9
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

        self.Map1 = None

        self.physic_engine = None
        self.Left_pressed = None
        self.Right_pressed = None


    def setup(self):
        #LOad the map into the program
        self.Map1 = arcade.load_tilemap("map1.json",1)
        print("Available sprite lists:", self.Map1.sprite_lists.keys())
        #load all the map layers into the initialized obj
        self.bg = self.Map1.sprite_lists["bgg"]
        self.ground = self.Map1.sprite_lists["ground"]
        #self.obstacle = self.Map1.sprite_lists["obstacle"]
        self.item = self.Map1.sprite_lists["decor-back"]
        self.item2 = self.Map1.sprite_lists["decor-more"]
        self.item3 = self.Map1.sprite_lists["decor-up"]



        self.player = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk5.png", 0.2)
        self.player.center_x = 4 * tileSize
        self.player.center_y = 13 * tileSize

        self.physic_engine = arcade.PhysicsEnginePlatformer(self.player, self.ground)




    def on_draw(self):
        arcade.start_render()

        self.bg.draw()
        self.item.draw()
        self.ground.draw()
        self.item2.draw()
        self.item3.draw()
        self.player.draw()

    def on_update(self, delta_time: float):
        self.physic_engine.update()

        # Set player's velocity based on key presses
        if self.Left_pressed and not self.Right_pressed:
            self.player.change_x = -MovementSpeed
        elif self.Right_pressed and not self.Left_pressed:
            self.player.change_x = MovementSpeed
        else:
            self.player.change_x = 0

        # Adjust player's position to stay within the window
        self.player.update()

        # Check if the player is going off the left or right side of the window
        if self.player.left < 0:
            self.player.left = 0
        elif self.player.right > self.Map1.width * tileSize:  # Adjusted for map width
            self.player.right = self.Map1.width * tileSize  # Adjusted for map width

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.Left_pressed = True
        elif key == arcade.key.RIGHT:
            self.Right_pressed =True
        elif key == arcade.key.UP:
            if self.physic_engine.can_jump():
                self.player.change_y = JumpSpeed

    def on_key_release(self, key, modifiers: int):
        if key == arcade.key.LEFT:
            self.Left_pressed = False
        elif key == arcade.key.RIGHT:
            self.Right_pressed =False

map1 = myMaps()
map1.setup()
arcade.run()