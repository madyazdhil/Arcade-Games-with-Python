import arcade

#var to store the size of win

WIN_HEIGHT = 640
WIN_WIDTH = 640

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        #set the bg - color
        arcade.set_background_color(arcade.color.BISQUE)

        #var to store the X and the Y
        self.ball_x = 50
        self.ball_y = 50

        #to make the mouse pointer invicible
        self.set_mouse_visible(False)

    #function to display everything
    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x,self.ball_y,15,arcade.color.RED)

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball_x = x
        self.ball_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            print(f"the Left mouse button clicked at X={x} Y={y} ")
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print(f"the Right mouse button clicked at X={x} Y={y} ")


def main():
    win = MyGame(WIN_WIDTH,WIN_HEIGHT,"My first Arcade")
    arcade.run()

main()

