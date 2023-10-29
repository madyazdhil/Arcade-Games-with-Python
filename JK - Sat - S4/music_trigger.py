import arcade

arcade.open_window(200,200,"Music")
sound = arcade.load_sound("soundtrack.mp3")

arcade.play_sound(sound)
arcade.run()