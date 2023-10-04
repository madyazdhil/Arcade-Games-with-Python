#creating the bluprint or cetakan
class car:
    #inisiasi hal apa saja yang ada di dalam objek mobil
    def __init__(self, model, colour, seat, year):
        self.model = model
        self.colour = colour
        self.seat = seat
        self.year = year

    #membuat methode / fungsi bekerja dari suatu objek
    def tentangMobil(self):
        return f"Mobil ini dibuat tahun {self.year} dan memiliki kapasitas {self.seat} orang"

    def beban(self):
        return f"Mobil tipe {self.model} mempunyai beban sebanyak 3 ton"


Mb001 = car("Sedan","Merah", 7, 2022)
Mb002 = car("MPV", "Silver", 8, 2022)

print(Mb001.tentangMobil())
print(Mb002.beban())