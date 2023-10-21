import arcade

arcade.open_window(300,300,"A window with sound")
soundbg = arcade.load_sound("soundtrack.mp3")

arcade.play_sound(soundbg)
arcade.run()