import arcade

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.ball_x = 100
        self.ball_y = 100

        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x,self.ball_y,15, arcade.color.RED)

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball_x = x
        self.ball_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print(f"Left button has been pressed in coordinate {x}, {y}")
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print(f"Right button has been pressed in coordinate {x}, {y}")

def main():
    win1 = Game(600,600,"My first Arcade in Class")
    arcade.run()


main()
