import arcade

#creating window with it's sizes and title
arcade.open_window(600,600,"Landscaping")

#set background colour
arcade.set_background_color(arcade.color.SKY_BLUE)

#memulai proses rendering
arcade.start_render()

#land
arcade.draw_lrtb_rectangle_filled(0,600,300,0,arcade.color.ARMY_GREEN)

#pohon1 - circle

#batang
arcade.draw_rectangle_filled(100, 315, 20, 50, arcade.color.COCOA_BROWN)
#daun circle
arcade.draw_circle_filled(100,335,20,arcade.csscolor.FOREST_GREEN)


#pohon2
arcade.draw_rectangle_filled(200, 315, 20, 50, arcade.color.COCOA_BROWN)
arcade.draw_ellipse_filled(200, 340, 35,43, arcade.color.FOREST_GREEN)

#pohon 3
arcade.draw_rectangle_filled(300, 315, 20, 50, arcade.color.COCOA_BROWN)
arcade.draw_arc_filled(300, 340,
                       50,50,
                       arcade.color.FOREST_GREEN,
                       0,180)


#pohon4
arcade.draw_rectangle_filled(400, 315, 20, 50, arcade.color.COCOA_BROWN)

#pohon 5
arcade.draw_rectangle_filled(500, 315, 20, 50, arcade.color.COCOA_BROWN)

#akhiri proses render
arcade.finish_render()

arcade.run()