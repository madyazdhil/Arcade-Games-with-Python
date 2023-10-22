import arcade

MOVEMENT = 1
WIDTH = 600
HEIGHT = 600

s1 = arcade.load_sound(":resources:sounds/laser4.wav")
s2 = arcade.load_sound(":resources:sounds/error5.wav")
s3 = arcade.load_sound(":resources:sounds/hit1.wav")
s4 = arcade.load_sound(":resources:sounds/jump5.wav")

class MyWindow(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.LION)

        self.ball_x = 100
        self.ball_y = 100
        self.move_x = 0
        self.move_y = 0


    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x,self.ball_y,15,arcade.color.WINE)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.move_y = MOVEMENT
            arcade.play_sound(s1)
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.move_y = -MOVEMENT
            arcade.play_sound(s2)
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.move_x = -MOVEMENT
            arcade.play_sound(s3)
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.move_x = MOVEMENT
            arcade.play_sound(s4)

    def on_key_release(self, key, modifiers):
        self.move_x = 0
        self.move_y = 0

    def on_update(self, delta_time):
        self.ball_x += self.move_x
        self.ball_y += self.move_y

def main():
    win1 = MyWindow(WIDTH,HEIGHT,"Controll the Ball")
    sound = arcade.load_sound("soundtrack.mp3")

    arcade.play_sound(sound)
    arcade.run()

main()