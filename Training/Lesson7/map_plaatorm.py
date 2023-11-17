import random

import arcade

TILE_SCALING = 1
GRID_PIXEL_SIZE = 70

DEFAULT_SCREEN_WIDTH = 15 * GRID_PIXEL_SIZE
DEFAULT_SCREEN_HEIGHT = 10 * GRID_PIXEL_SIZE
SCREEN_TITLE = "Dunia Permen"
PLAYER_MOVEMENT_SPEED = 2
GRAVITY = 1/2
JUMP_SPEED = 15


LEVELS = [
    "level1.json",
    "level2.json",
]

CHOOSE_LEVEL = random.choice(LEVELS)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)
        # digunakan untuk menampung list of sprite background dari tilemaps
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

    def setup(self):
        self.tile_map = arcade.load_tilemap("mapku.json", TILE_SCALING)
        self.background = self.tile_map.sprite_lists["bg"]
        #self.obstacles = self.tile_map.sprite_lists["obstacles"]
        self.ground = self.tile_map.sprite_lists["ground"]
        self.props = self.tile_map.sprite_lists["item"]
        #self.stars = self.tile_map.sprite_lists["stars"]
        self.players = arcade.Sprite(":resources:images/animated_characters/robot/robot_walk4.png", 1)
        self.players.center_x=100
        self.players.center_y=300

        #self.player = self.players[0]

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.background.draw()
        #self.obstacles.draw()
        self.ground.draw()
        self.props.draw()
        #self.stars.draw()
        self.players.draw()



window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()