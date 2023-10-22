import arcade

class MyWindow(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.LION)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(100,100,15,arcade.color.WINE)


def main():
    win1 = MyWindow(600,600,"My first arcade OOP")
    arcade.run()

main()