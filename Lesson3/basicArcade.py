#import module
import arcade

# Open the window. Set the window title and
# dimensions (width and height)
arcade.open_window(600, 600, "Draw an arc for GfG ")

#set background
arcade.set_background_color(arcade.color.WHITE)

# Start the render process.
arcade.start_render()

#function to draw a circle
arcade.draw_circle_outline(300, 285, 88, arcade.color.GREEN, 9,-1)

#finish drawing
arcade.finish_render()

#to display everything
arcade.run()
