import arcade

class Game(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "Physics Engine")

        #initiate the velocity
        self.velocityx = 0

        #initiate the scene object
        self.scene = None

        #character
        self.player =  None

        #for the physics engine
        self.physicsEngine = None
        self.colitionBox = None



    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.SKY_BLUE)

        #Draw or make the scene appears
        self.scene.draw()



    #function to set up the game
    def setup(self):
        #insert value ke scene object
        self.scene = arcade.Scene()

        #listing the sprites
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Ground")


        ##PLAYER
        #Inserting caharcters to sprites
        self.player = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_walk1.png",1)
        #set the location
        self.player.center_x = 300
        self.player.center_y = 600
        #insert the sprites to the scene
        self.scene.add_sprite("Player", self.player)

        ##platform / place that hold the player
        platform = arcade.Sprite("ground.png",1)
        platform.center_x=300
        platform.center_y=70
        self.scene.add_sprite("Ground", platform)


        ##PHYSICS ENGINE
        self.physicsEngine = arcade.PhysicsEnginePlatformer(
            self.player,self.scene.get_sprite_list("Ground")
        )

        self.colitionBox = arcade.PhysicsEngineSimple(
            self.player, self.scene.get_sprite_list("Ground")
        )


    def on_update(self, delta_time):
        self.player.center_x += self.velocityx * delta_time
        self.physicsEngine.update()
        self.colitionBox.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.velocityx = -100
        elif key == arcade.key.RIGHT:
            self.velocityx = 100

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.velocityx = 0
        elif key == arcade.key.RIGHT:
            self.velocityx = 0


Scene1 = Game()
Scene1.setup()
arcade.run()

