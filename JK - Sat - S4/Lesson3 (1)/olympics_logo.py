import arcade

#creating window with it's sizes and title
arcade.open_window(600,600,"My first Window")

#set background colour
arcade.set_background_color(arcade.color.WHITE)

#memulai proses rendering
arcade.start_render()

#create the first circle - black
arcade.draw_circle_outline(300,300,77,arcade.csscolor.BLACK, 5)


#akhiri proses render
arcade.finish_render()

arcade.run()