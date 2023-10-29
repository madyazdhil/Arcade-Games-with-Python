import arcade

class Game(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Is it working")

        #attributes
        self.velx = 0
        self.scene = None
        self.ply1 = None
        self.physics_en = None
        self.box_col = None

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.scene.draw()

    def setup(self):
        self.scene = arcade.Scene()

        # Sprites
        self.scene.add_sprite_list("player")
        self.scene.add_sprite_list("ground", use_spatial_hash=True)

        # Player
        self.ply1 = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png", 1)
        self.ply1.center_y = 300
        self.ply1.center_x = 300
        self.scene.add_sprite("player", self.ply1)


        # Platform
        platform = arcade.Sprite("ground.png",1)
        platform.center_y = 40
        self.scene.add_sprite("ground", platform)

        #self.physics_en = arcade.PhysicsEnginePlatformer(self.ply1, self.scene.get_sprite_list("ground"))
        #self.box_col = arcade.PhysicsEngineSimple(self.ply1, self.scene.get_sprite_list("ground"))



    # def on_update(self, delta_time):
    #     self.ply1.center_x += self.velx * delta_time
    #     self.physics_en.update()
    #     self.box_col.update()


g1 = Game()
g1.setup()
arcade.run()
