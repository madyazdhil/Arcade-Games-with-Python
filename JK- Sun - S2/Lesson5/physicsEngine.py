import arcade

class myGame(arcade.Window):
    def __init__(self):
        super().__init__(600,600,"Physics Engine")

        self.sprite = None
        self.sprite2 = None

        self.scene = None


    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.scene.draw()

    def setup(self):
        # adding the sprite image

        self.scene = arcade.Scene()

        self.sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk6.png")
        self.sprite.center_x = 160
        self.sprite.center_y = 300
        self.scene.add_sprite("player",self.sprite)


        self.sprite2 = arcade.Sprite("alien.png",0.2)
        self.sprite2.center_x = 450
        self.sprite2.center_y = 300
        self.scene.add_sprite("player 2", self.sprite2)



window1 = myGame()
window1.setup()
arcade.run()
