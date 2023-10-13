#import the arcade module
import arcade

#setting the width and the height of the game's window + title
arcade.open_window(600,600,"Olympics Logo")

#setting the bg color
arcade.set_background_color(arcade.color.WHITE)


###render = displaying everything inside the arcade window

#starting the rendering process
arcade.start_render()

#everything will be inside the strat render - between start and end
arcade.draw_circle_outline(300, 300, 50,arcade.csscolor.BLACK,6)
arcade.draw_line()

#finishing rendering
arcade.finish_render()


#displaying the console and it's content continously
arcade.run()