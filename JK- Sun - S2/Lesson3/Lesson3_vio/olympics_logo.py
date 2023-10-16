import arcade

#creating a window with sizes and title
arcade.open_window(600,600,"Olympics Logo")

#setting the BG color
arcade.set_background_color(arcade.color.WHITE)

### render

#1. start the render
arcade.start_render()

#2.Commands
arcade.draw_circle_outline(300,300,65,arcade.color.BLACK,5)
arcade.draw_circle_outline(150,300,65,arcade.color.BLUE,5)
arcade.draw_circle_outline(450,300,65,arcade.color.RED,5)
arcade.draw_circle_outline(225,220,65,arcade.color.YELLOW,5)
arcade.draw_circle_outline(375,220,65,arcade.color.APPLE_GREEN,5)


#3. finish the render
arcade.finish_render()

#showing the window all the time
arcade.run()