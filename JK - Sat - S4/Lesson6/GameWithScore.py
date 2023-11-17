import random

import arcade

WinHd = 600
WinWd = 600

class Mygame(arcade.Window):
    def __init__(self):
        super().__init__(WinWd,WinHd, "Shooting Game")

        #iniate the sprites
        self.spritePlayer = None
        self.spriteCoin = None

        #lists = to store the lists of sprites
        self.spriteList = None
        self.CoinLists = None

        #to store the Score
        self.score = None

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.OUTER_SPACE)

    def setup(self):

        #giving a data to the attributes
        self.spriteList = arcade.SpriteList()
        self.CoinLists = arcade.SpriteList()

        #score
        self.score = 0

        #inserting the picture to the sprite

        ##spaceship
        self.spritePlayer = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png", 0.5)
        self.spritePlayer.center_x = 300
        self.spritePlayer.center_y = 300
        self.spriteList.append(self.spritePlayer)

        ##coin

        for i in range(50):

            coin = arcade.Sprite(":resources:images/alien/alienBlue_walk2.png", 0.2)
            coin.center_x = random.randrange(WinWd)
            coin.center_y = random.randrange(WinHd)
            self.CoinLists.append(coin)


    def on_draw(self):
        arcade.start_render()

        self.spriteList.draw()
        self.CoinLists.draw()

        txt = f"Alien Abducted = {self.score}"
        arcade.draw_text(
            txt,
            30,
            30,
            arcade.color.WHITE,
            15
        )

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.spritePlayer.center_x = x
        self.spritePlayer.center_y = y

    def update(self, delta_time):

        self.CoinLists.update()

        coinHitList = arcade.check_for_collision_with_list(
            self.spritePlayer,
            self.CoinLists
        )

        for coin in coinHitList:
            coin.remove_from_sprite_lists()
            self.score += 1


screen1 = Mygame()
screen1.setup()
arcade.run()

