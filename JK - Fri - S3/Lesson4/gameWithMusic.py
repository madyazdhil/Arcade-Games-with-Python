import arcade

# var to store the size of win

WIN_HEIGHT = 640
WIN_WIDTH = 640

MOVEMENT = 3

sound1 = arcade.load_sound(":resources:sounds/jump5.wav")
sound2 = arcade.load_sound(":resources:sounds/error2.wav")

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # set the bg - color
        arcade.set_background_color(arcade.color.BISQUE)

        self.ball_x = 50
        self.ball_y = 50
        self.change_y = 0
        self.change_x = 0

    # function to display everything
    def on_draw(self):
        arcade.start_render()

        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.RED)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.change_y = MOVEMENT
            arcade.play_sound(sound1)
        elif key == arcade.key.S:
            self.change_y = -MOVEMENT
            arcade.play_sound(sound1)
        elif key == arcade.key.A:
            self.change_x = -MOVEMENT
            arcade.play_sound(sound2)
        elif key == arcade.key.D:
            self.change_x = MOVEMENT
            arcade.play_sound(sound2)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.change_x = 0

    def on_update(self, delta_time):
        self.ball_x += self.change_x
        self.ball_y += self.change_y


def main():
    win = MyGame(WIN_WIDTH, WIN_HEIGHT, "My first Arcade")
    soundbg = arcade.load_sound("soundtrack.mp3")
    arcade.play_sound(soundbg)
    arcade.run()


main()

