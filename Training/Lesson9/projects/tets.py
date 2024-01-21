import random

import arcade
from players import PlayerCharacter

TILE_SCALING = 1
GRID_PIXEL_SIZE = 70

DEFAULT_SCREEN_WIDTH = 15 * GRID_PIXEL_SIZE
DEFAULT_SCREEN_HEIGHT = 10 * GRID_PIXEL_SIZE
SCREEN_TITLE = "Dunia Permen"
PLAYER_MOVEMENT_SPEED = 2
GRAVITY = 1/2
JUMP_SPEED = 10


LEVELS = [
    "level1.json",
    "level2.json",
]

CHOOSE_LEVEL = random.choice(LEVELS)


COIN_SCALE = 0.5
COIN_COUNT = 50
CHARACTER_SCALING = 1

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)
        self.background = None
        self.obstacles = None
        self.ground = None
        self.props = None
        self.stars = None
        self.players = None
        self.player = None

        self.tile_map = None

        self.physic_engine = None
        self.left_pressed = None
        self.right_pressed = None
        self.score = 0

        self.background_sound = arcade.load_sound("assets/sounds/supermario.mp3")
        self.item_sound = arcade.load_sound('assets/sounds/coin.mp3')
        self.jump_sound = arcade.load_sound('assets/sounds/jump.wav')
        self.die_sound = arcade.load_sound('assets/sounds/die.wav')
        self.play_sound_bg = arcade.play_sound(self.background_sound, volume=0.1)

    def setup(self):
        self.tile_map = arcade.load_tilemap('level1.json', scaling=TILE_SCALING)
        self.background = self.tile_map.sprite_lists["background"]
        self.obstacles = self.tile_map.sprite_lists["obstacles"]
        self.ground = self.tile_map.sprite_lists["ground"]
        self.props = self.tile_map.sprite_lists["props"]
        self.stars = self.tile_map.sprite_lists["stars"]
        # self.players = self.tile_map.sprite_lists['players']
        # self.player = self.players[0]

        # self.players = arcade.SpriteList()
        #
        # # Set up the player
        # self.player = PlayerCharacter()
        #
        # self.player.center_x = DEFAULT_SCREEN_WIDTH // 3
        # self.player.center_y = DEFAULT_SCREEN_HEIGHT // 3
        # self.player.scale = 0.8
        #
        # self.players.append(self.player)

        self.player = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk5.png", 0.8)
        self.player.center_x = 4 * GRID_PIXEL_SIZE
        self.player.center_y = 13 * GRID_PIXEL_SIZE

        self.physic_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            self.ground,
            gravity_constant=GRAVITY
        )

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.background.draw()
        self.obstacles.draw()
        self.ground.draw()
        self.props.draw()
        self.stars.draw()
        self.player.draw()
        # self.physic_engine.update()
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.BLACK_BEAN, 14)

    def on_update(self, delta_time: float):
        self.player.change_x = 0
        # self.player_sprite.change_y = 0



        if self.left_pressed and not self.right_pressed:
            self.player.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player.change_x = PLAYER_MOVEMENT_SPEED

        # Move the player
        #self.players.update()

        # Update the players animation
        #self.players.update_animation()

        self.physic_engine.update()

        # game 09
        star_hit = arcade.check_for_collision_with_list(
            self.player,
            self.stars
        )

        obstacle_hit = arcade.check_for_collision_with_list(
            self.player,
            self.obstacles
        )

        if obstacle_hit:
            self.player.change_y = 150
            self.player.center_x = self.player.center_x - 50
            self.player.center_y = self.player.center_y + 90

            for i in obstacle_hit:
                self.score = 0
                arcade.stop_sound(self.play_sound_bg)
                arcade.play_sound(self.die_sound)
                self.player.remove_from_sprite_lists()

        if star_hit:
            for star in star_hit:
                star.remove_from_sprite_lists()
                self.score += 1

                arcade.play_sound(self.item_sound)

        #
        # if star_hit:
        #     for star in star_hit:
        #         star.remove_from_sprite_li    sts()
        # sound
        # scoring
        # obstacle hit
        # move screen

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            if self.physic_engine.can_jump():
                arcade.play_sound(self.jump_sound)
                self.player.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False


window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()