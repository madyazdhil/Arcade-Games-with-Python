import arcade

class MyWindow(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.LION)

        self.ball_x = 100
        self.ball_y = 100
        self.ball2_x = 100
        self.ball2_y = 100

        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x,self.ball_y,15,arcade.color.WINE)
        arcade.draw_circle_filled(self.ball2_x,self.ball2_y,15,arcade.color.GUPPIE_GREEN)

    def on_mouse_motion(self, x, y, dx, dy):
        self.ball_x = x
        self.ball_y = y

    def on_update(self, delta_time):
        self.ball2_x +=1
        self.ball2_y +=1

def main():
    win1 = MyWindow(600,600,"The object Following Pointers")
    arcade.run()

main()