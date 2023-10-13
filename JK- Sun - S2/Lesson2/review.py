class apple:
    def __init__(self, warna, musim_panen, asal):
        self.warna = warna
        self.musim_panen = musim_panen
        self.asal = asal

    def aboutapple(self):
        print(f"apple ini berasal dari {self.asal} yang biasanya berwarna {self.warna} dan dipanen pada musim {self.musim_panen}")


apple11 = apple("Merah","Hujan", "Malang")
apple11.aboutapple()

class strawberry:
    def __init__(self, warna, musimPanen, ExpDate):
        self.warna = warna
        self.panen = musimPanen
        self.expire = ExpDate

    def aboutStr(self):
        print(f"This strawberry is Expired in {self.expire}, because it was harvested in {self.panen}. it really georgeus because of it's {self.warna} Colour")

str1 = strawberry("merah, Kemarau",musimPanen="21 maret 2024")