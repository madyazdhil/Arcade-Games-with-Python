import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 3

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

        # First dot controlled by arrow keys
        self.position_x = 50
        self.position_y = 50
        self.radius = 15
        self.color = arcade.color.RED
        self.change_x = 0
        self.change_y = 0

        # Second dot controlled by WASD keys
        self.position_x_2 = 100
        self.position_y_2 = 100
        self.radius_2 = 15
        self.color_2 = arcade.color.BLUE
        self.change_x_2 = 0
        self.change_y_2 = 0

        self.set_mouse_visible(False)

    def on_draw(self):
        arcade.start_render()

        # Draw the first dot
        arcade.draw_circle_filled(
            self.position_x,
            self.position_y,
            self.radius,
            self.color
        )

        # Draw the second dot
        arcade.draw_circle_filled(
            self.position_x_2,
            self.position_y_2,
            self.radius_2,
            self.color_2
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.change_y = -MOVEMENT_SPEED

        # WASD keys for the second dot
        elif key == arcade.key.A:
            self.change_x_2 = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.change_x_2 = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.change_y_2 = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.change_y_2 = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.change_y = 0

        # Release WASD keys for the second dot
        elif key in (arcade.key.A, arcade.key.D):
            self.change_x_2 = 0
        elif key in (arcade.key.W, arcade.key.S):
            self.change_y_2 = 0

    def update(self, delta_time):
        # Move the first dot
        self.position_y += self.change_y
        self.position_x += self.change_x

        # Move the second dot
        self.position_y_2 += self.change_y_2
        self.position_x_2 += self.change_x_2

def main():
    window = MyGame(640, 480, "Two Dots Example")
    arcade.run()

main()
