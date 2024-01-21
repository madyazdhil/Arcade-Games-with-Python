import arcade

#speed for changing frames
anim_speed = 5

#var to check whether its facing left or right
Right_looking = 0
Left_looking = 1

def load_pair(filename):

    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]

class PlayerCharacter(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.character_facing = Right_looking

        self.current_texture = 0

        self.scale = 0.2

        #bounding box
        self.points = [[-22, -64], [22, -64], [22, 28], [-22,-28]]

        main_path = ":resources:images/animated_characters/robot"

        self.iddle_pict = load_pair(f"{main_path}_idle.png")

        #adding the frames of it walking
        self.walking_pict = []
        for i in range(8):
            frames = load_pair(f"{main_path}_walk{i}.png")
            self.walking_pict.append(frames)

    def update_animation(self, delta_time: float = 1 / 60):
        #animation for looking right left
        if self.change_x < 0 and self.character_facing == Right_looking:
            self.character_facing = Left_looking
        elif self.change_x > 0 and self.character_facing == Left_looking:
            self.character_facing = Right_looking

        #walking
        self.current_texture += 1
        if self.current_texture >7 * anim_speed:
            self.current_texture = 0

        frame = self.current_texture // anim_speed
        direction = self.character_facing
        self.texture = self.walking_pict[frame][direction]

        # Idle animation
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.iddle_pict[self.character_facing]
            return