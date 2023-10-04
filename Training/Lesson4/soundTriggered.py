import arcade
import pyglet

class MyApplication(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Trigger Sound With Key")

        # Initialize a flag to track whether the sound is currently playing
        self.sound_playing = False

        # Load the sound when the application starts
        self.laser_sound = pyglet.media.load("soundtrack.mp3")

        # Create a pyglet.media.Player to play the sound
        self.sound_player = pyglet.media.Player()

    def on_key_press(self, key, modifiers):

        # Check if the sound is not currently playing
        if key == arcade.key.SPACE and not self.sound_playing:
            # Queue the sound to the player and play it
            self.sound_player.queue(self.laser_sound)
            self.sound_player.play()

            # Set the flag to indicate that the sound is playing
            self.sound_playing = True

    def on_update(self, delta_time):
        # Check if the sound has finished playing
        if self.sound_playing and not self.sound_player.playing:
            # Update the flag to indicate that the sound is not playing
            self.sound_playing = False

def main():
    window = MyApplication(300, 300)
    arcade.run()

if __name__ == "__main__":
    main()
