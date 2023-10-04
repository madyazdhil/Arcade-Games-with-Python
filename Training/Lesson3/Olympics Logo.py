# import module
import arcade

# Open the window. Set the window title and
# dimensions (width and height)
arcade.open_window(600, 600, "Draw  an arc  for GfG ")

# set background color
arcade.set_background_color(arcade.color.WHITE)

# Start the render process.
arcade.start_render()

# function for designing olympic flag
arcade.draw_circle_outline(100, 285, 88, arcade.color.BLUE, 9, -1)
arcade.draw_circle_outline(300, 285, 88, arcade.color.BLACK, 9, -1)
arcade.draw_circle_outline(500, 285, 88, arcade.color.RED, 9, -1)
arcade.draw_circle_outline(200, 185, 88, arcade.color.YELLOW, 9, -1)
arcade.draw_circle_outline(400, 185, 88, arcade.color.GREEN, 9, -1)

# finished drawing
arcade.finish_render()

# to display everything
arcade.run()