#import the arcade module
import arcade

#setting the width and the height of the game's window + title
arcade.open_window(600, 600, "Snowman")

#setting the bg color
arcade.set_background_color(arcade.color.SKY_BLUE)

###render = displaying everything inside the arcade window

#starting the rendering process
arcade.start_render()

# draw the snowman
arcade.draw_circle_filled(300, 350, 60, arcade.color.WHITE)  # bottom circle
arcade.draw_circle_filled(300, 250, 80, arcade.color.WHITE)  # middle circle
arcade.draw_circle_filled(300, 435, 40, arcade.color.WHITE)  # top circle

# draw the stick hand
arcade.draw_line(330, 575, 360, 575, arcade.color.BLACK, 4)

# draw the nose
arcade.draw_triangle_filled(300, 625, 290, 605, 310, 605, arcade.color.ORANGE)

arcade.draw_triangle_filled(300,440,
                            300,430,
                            370,435,
                            arcade.color.ORANGE_PEEL)

#finishing rendering
arcade.finish_render()

#displaying the console and its content continuously
arcade.run()
