#import module
import arcade

#open a new window, and sets the dimension and title
arcade.open_window(600,600,"Olympic's Logo")

#colour the bg
arcade.set_background_color(arcade.color.WHITE)

#what ever we wanted in that window MUST be inside or below the start render
arcade.start_render()

arcade.draw_circle_outline(300,300,60, arcade.color.BLACK,9)
arcade.draw_circle_outline(150,300,60, arcade.color.BLUE,9)
arcade.draw_circle_outline(450,300,60, arcade.color.RED,9)

arcade.finish_render()

arcade.run()