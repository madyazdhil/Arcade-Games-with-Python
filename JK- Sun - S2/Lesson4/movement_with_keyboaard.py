import arcade

MOVEMENT = 5
sound1 = arcade.load_sound(":resources:sounds/laser3.wav")


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.ball_x = 100
        self.ball_y = 100

        self.move_x = 0
        self.move_y = 0

        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x,self.ball_y,15, arcade.color.RED)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.move_y = MOVEMENT
            arcade.play_sound(sound1)
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.move_y = -MOVEMENT
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.move_x = MOVEMENT
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.move_x = -MOVEMENT

    def on_key_release(self, key, modifiers):
        self.move_x = 0
        self.move_y = 0

    def on_update(self, delta_time):
        self.ball_x += self.move_x
        self.ball_y += self.move_y
def main():
    win1 = Game(600,600,"My first Arcade in Class")
    bg_sound = arcade.load_sound("soundtrack.mp3")

    arcade.play_sound(bg_sound)
    arcade.run()


main()
