import arcade

class game(arcade.Window):
    def __init__(self):
        super().__init__(600,600,"Character With Physics Engine")

        #buat attribut untuk menyimpan kecepetan berpindah
        self.velocity = 0

        #memerlukan scene == character apasaja yg muncuul pada scenario tertentu
        #tambahkan attribut untuk menampung scene
        self. scene = None

        #attribubts to store the player
        self.player = None

        self.physicsengine = None
        self.box_collision = None

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)
        self.scene.draw()

    def setup(self):

        #initialize scene object
        self.scene = arcade.Scene()

        #create lists untuk menampung sprite
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Ground", use_spatial_hash=True)

        #adding the sprite image
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png", 1)

        #location of the sprite
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 300

        #memasukkan sprite kedalam scene
        self.scene.add_sprite_list("Player",self.player_sprite)


        #ground sprite
        ground = arcade.Sprite("ground.png")
        ground.center_x = 300
        ground.center_y = 300

        self.scene.add_sprite_list("Ground", ground)

        ###creating the PHYSICS ENGINE
        self.physicsengine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.scene.get_sprite_list("Ground")
        )

        self.box_collision = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Ground")
        )






scene1 = game()
scene1.setup()
arcade.run()
