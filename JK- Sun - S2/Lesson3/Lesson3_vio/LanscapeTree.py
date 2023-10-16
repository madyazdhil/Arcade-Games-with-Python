import arcade

#creating a window with sizes and title
arcade.open_window(600,600,"Landscape with Trees")

#setting the BG color
arcade.set_background_color(arcade.color.SKY_BLUE)

### render

#1. start the render
arcade.start_render()

#2.Commands
arcade.draw_lrtb_rectangle_filled(0,600,300,0,arcade.color.FERN_GREEN)


#tree1
arcade.draw_rectangle_filled(100,320,20,50,arcade.color.WOOD_BROWN)
arcade.draw_circle_filled(100,335,20,arcade.color.GUPPIE_GREEN)


#tree2
arcade.draw_rectangle_filled(200,320,20,50,arcade.color.WOOD_BROWN)
arcade.draw_ellipse_filled(200,360,40,50,arcade.color.GUPPIE_GREEN)


#tree3
arcade.draw_rectangle_filled(300,320,20,50,arcade.color.WOOD_BROWN)
arcade.draw_arc_filled(300,340,50,50,arcade.color.GUPPIE_GREEN,0,180)


#tree4
arcade.draw_rectangle_filled(400,320,20,50,arcade.color.WOOD_BROWN)
arcade.draw_triangle_filled(400,400,360,320,440,320,arcade.color.GUPPIE_GREEN)


#tree5
arcade.draw_rectangle_filled(500,320,20,50,arcade.color.WOOD_BROWN)



#3. finish the render
arcade.finish_render()

#showing the window all the time
arcade.run()