class Volume:
    def __init__(self, length, height, width, radius):
        self.lenght = length
        self.height = height
        self.width = width
        self.radius = radius

    def VolumeCube(self):
        volume = self.lenght**3
        return f"The volume of the cube with the lenght of {self.lenght} is {volume}"

    def VolumeBlock(self):
        volume = self.lenght*self.width*self.height
        return f"The block Volume is {volume}"

    def cylinder(self):
        v = 3.14*self.radius*self.radius*self.height
        return f"The cylinder volume is {v}"

O1 = Volume(None, 14,None,7)
print(O1.cylinder())
