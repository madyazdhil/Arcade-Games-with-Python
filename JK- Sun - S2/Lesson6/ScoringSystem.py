import random

import arcade

widthScreen = 600
heightScreen = 600
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(widthScreen,heightScreen,"Space Invasion")

        self.Spaceship = None
        self.planets = None

        self.SpaceshipList = None
        self.planetsList = None

        self.score = 0

        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.SPACE_CADET)
        self.SpaceshipList.draw()
        self.planetsList.draw()

        txt = f"Planets Collected = {self.score}"
        arcade.draw_text(
            txt,
            30,
            570,
            arcade.color.WHITE,
            15
        )


    def setup(self):

        self.SpaceshipList = arcade.SpriteList()
        self.planetsList = arcade.SpriteList()

        self.Spaceship = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png", 0.5)
        self.Spaceship.center_x = 300
        self.Spaceship.center_y = 300
        self.SpaceshipList.append(self.Spaceship)

        for i in range(55):

            planet = arcade.Sprite(":resources:images/topdown_tanks/treeGreen_small.png", 0.7)
            planet.center_x = random.randrange(widthScreen)
            planet.center_y = random.randrange(heightScreen)
            self.planetsList.append(planet)


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.Spaceship.center_x = x
        self.Spaceship.center_y = y

    def update(self, delta_time: float):
        self.planetsList.update()

        check_Whos_touching = arcade.check_for_collision_with_list(self.Spaceship, self.planetsList)

        for planet in check_Whos_touching:
            planet.remove_from_sprite_lists()
            self.score += 1


battleground1 = MyGame()
battleground1.setup()
arcade.run()
