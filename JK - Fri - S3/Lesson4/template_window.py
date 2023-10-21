import arcade

#var to store the size of win

WIN_HEIGHT = 640
WIN_WIDTH = 640

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        #set the bg - color
        arcade.set_background_color(arcade.color.BISQUE)

        self.ball_x = 50
        self.ball_y = 50

    #function to display everything
    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x,self.ball_y,15,arcade.color.RED)

    def on_update(self, delta_time):
        self.ball_y += 1


def main():
    win = MyGame(WIN_WIDTH,WIN_HEIGHT,"My first Arcade")
    arcade.run()

main()

