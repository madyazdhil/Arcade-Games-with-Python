# Importing arcade module
import arcade


# Creating MainGame class
class MainGame(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, title="Player Movement")

        # Initializing a variable to store
        # the velocity of the player
        self.vel_x = 0

        # Creating scene object
        self.scene = None

        # Creating variable to store player sprite
        self.player = None

        # Creating variable for our game engine
        self.physics_engine = None
        self.box_collision = None

    # Creating on_draw() function to draw on the screen
    def on_draw(self):
        arcade.start_render()

        # Drawing our scene
        self.scene.draw()

    def setup(self):

        # Initialize Scene object
        self.scene = arcade.Scene()

        # Creating different sprite lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Platforms", use_spatial_hash=True)
        self.scene.add_sprite_list("Enemies", use_spatial_hash=True)

        # Adding player sprite
        self.player_sprite = arcade.Sprite("monster-right.png", 1)


        # Adding coordinates for the center of the sprite
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 600

        # Adding Sprite in our scene
        self.scene.add_sprite("Player", self.player_sprite)

        self.player_sprite_2 = arcade.Sprite("monster-left.png", 1)
        self.player_sprite_2.center_x = 64
        self.player_sprite_2.center_y = 600

        self.scene.add_sprite("Enemies", self.player_sprite_2)

        # Adding platform sprite
        platform = arcade.Sprite("floor.png", 1)

        # Adding coordinates for the center of the platform
        platform.center_x = 300
        platform.center_y = 32
        self.scene.add_sprite("Platforms", platform)

        # Creating Physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, self.scene.get_sprite_list("Platforms"), 0.5
        )

        self.physics_engine_2 = arcade.PhysicsEnginePlatformer(
            self.player_sprite_2, self.scene.get_sprite_list("Platforms"), 0.5
        )

        self.box_collision = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Platforms")
        )

        # if self.box_collision:
        #     print("ups!")

    # Creating on_update function to
    # update the x coordinate
    def on_update(self, delta_time):

        # Changing x coordinate of player
        self.player_sprite.center_x += self.vel_x * delta_time

        # Updating the physics engine to move the player
        self.physics_engine.update()
        self.physics_engine_2.update()
        self.box_collision.update()

    # Creating function to change the velocity
    # when button is pressed
    def on_key_press(self, symbol, modifier):

        # Checking the button pressed
        # and changing the value of velocity
        if symbol == arcade.key.LEFT:
            self.vel_x = -300
        elif symbol == arcade.key.RIGHT:
            self.vel_x = 300

    # Creating function to change the velocity
    # when button is released
    def on_key_release(self, symbol, modifier):

        # Checking the button released
        # and changing the value of velocity
        if symbol == arcade.key.LEFT:
            self.vel_x = 0
        elif symbol == arcade.key.RIGHT:
            self.vel_x = 0


# Calling MainGame class
game = MainGame()
game.setup()
arcade.run()