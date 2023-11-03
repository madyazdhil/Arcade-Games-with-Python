import random

import arcade

class mygame(arcade.Window):
    def __init__(self):
        super().__init__(600, 600, "SPace shooter")
        self.player = None
        self.score = None

        self.spriteList = None
        self.coinList = None

        self.set_mouse_visible(False)


    def setup(self):
        self.spriteList = arcade.SpriteList()
        self.coinList = arcade.SpriteList()

        self.score = 0

        self.player = arcade.Sprite(":resources:images/animated_characters/male_adventurer/maleAdventurer_jump.png", 0.5)
        self.player.center_x = 300
        self.player.center_y = 300
        self.spriteList.append(self.player)

        for i in range(50):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", 0.3)

            coin.center_x = random.randrange(600)
            coin.center_y = random.randrange(600)

            self.coinList.append(coin)

    def on_draw(self):
        arcade.set_background_color(arcade.color.PALE_GREEN)
        arcade.start_render()

        self.spriteList.draw()
        self.coinList.draw()

        textnya = f"Score you got = {self.score}"
        arcade.draw_text(textnya, 20,20, arcade.color.WHITE,20)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.player.center_x = x
        self.player.center_y = y


    def update(self, delta_time: float):

        self.coinList.update()

        coin_in_hit_list = arcade.check_for_collision_with_list(
            self.spriteList,self.coinList
        )

        for coin in coin_in_hit_list:
            coin.remove_from_sprite_lists()
            self.score +=1


window = mygame()
window.setup()
arcade.run()