import arcade

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(100,100,15, arcade.color.RED)


def main():
    win1 = Game(600,600,"My first Arcade in Class")
    arcade.run()


main()
