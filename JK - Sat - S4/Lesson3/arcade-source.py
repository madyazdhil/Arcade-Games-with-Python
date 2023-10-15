import arcade

#creating window with it's sizes and title
arcade.open_window(600,600,"My first Window")

#set background colour
arcade.set_background_color(arcade.color.WHITE)

#memulai proses rendering
arcade.start_render()


#akhiri proses render
arcade.finish_render()

arcade.run()