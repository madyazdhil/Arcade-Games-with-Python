import random

import arcade

SW = 600
SH = 600
class Mygame(arcade.Window):
    def __init__(self):
        super().__init__(SW, SH, "Space Ship Battle")

        #to store the sprites
        self.sprite = None
        self.coin = None

        #to save all the sprites into one storage
        ## LISTS

        self.spriteLists = None
        self.pointLists = None

        arcade.set_background_color(arcade.color.AMAZON)
        self.set_mouse_visible(False)


    def setup(self):

        #all the sprites
        self.spriteLists = arcade.SpriteList()
        self.pointLists = arcade.SpriteList()

        self.coin = 0

        ##importing all the sprites

        #player
        self.sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", 0.5)
        self.sprite.center_x = 300
        self.sprite.center_y = 300
        self.spriteLists.append(self.sprite)

        #coin

        #using loop to add the coin
        for i in range (50):
            coin = arcade.Sprite(":resources:images/items/star.png", 0.4)
            coin.center_x = random.randrange(SW)
            coin.center_y = random.randrange(SH)
            self.pointLists.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.spriteLists.draw()
        self.pointLists.draw()

        txt = f"Stars Collected = {self.coin}"
        arcade.draw_text(
            txt, 30,30, arcade.color.WHITE, 15
        )

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.sprite.center_x = x
        self.sprite.center_y = y

    def update(self, delta_time):

        #update the point lists
        self.pointLists.update()

        #mendefiniskan siapa saja yang tertabrak
        coin_hit_lists = arcade.check_for_collision_with_list(self.sprite,self.pointLists)

        #mengecek kondisinya - lakukan berulang
        for c1 in coin_hit_lists:
            #delete the touched coin from the list
            c1.remove_from_sprite_lists()
            #adding the score to the variable
            self.coin += 1



g1 = Mygame()
g1.setup()
arcade.run()
