import arcade as ac

ac.open_window(600,600,"Landscape")

ac.set_background_color(ac.csscolor.SKY_BLUE)

ac.start_render()

#Land
#left - Right - Top - Bottom
ac.draw_lrtb_rectangle_filled(0,600,300, 0,ac.csscolor.GREEN)

#tree #1
#trunk
ac.draw_rectangle_filled(100, 310, 20, 60,ac.color.SIENNA)
#leaves
ac.draw_circle_filled(100, 350, 25,ac.csscolor.DARK_GREEN)

#tree #2
#trunk
ac.draw_rectangle_filled(200, 310, 20, 60,ac.color.SIENNA)
#leaves
ac.draw_ellipse_filled(200,370,70,80,ac.color.DARK_SEA_GREEN)


#tree #3
#trunk
ac.draw_rectangle_filled(300, 310, 20, 60,ac.color.SIENNA)
#leaves
ac.draw_arc_filled(300, 330, 60,100, ac.color.DARK_ORCHID, 0,180)

#tree #4
#trunk
ac.draw_rectangle_filled(400, 310, 20, 60,ac.color.SIENNA)
#leaves
ac.draw_triangle_filled(400,400,370,320, 430,320,ac.color.DARK_VANILLA)


ac.finish_render()
ac.run()

