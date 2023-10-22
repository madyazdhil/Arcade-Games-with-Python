import arcade

class MyWindow(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.ball_x = 100
        self.ball_y = 100

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x,self.ball_y,15,arcade.color.WINE)


    def on_update(self, delta_time):
        self.ball_x +=1
        self.ball_y +=1

def main():
    win1 = MyWindow(600,600,"The Ball is moving by it's self")
    arcade.run()

main()