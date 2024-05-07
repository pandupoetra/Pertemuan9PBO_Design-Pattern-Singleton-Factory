from abc import ABC, abstractmethod
class Bentuk(ABC):
    def __init__(self, warna):
        self.warna = warna
    @abstractmethod
    def draw(self):
        pass
        
class Lingkaran(Bentuk):
    def __init__(self, warna, jari_jari):
        super().__init__(warna)
        self.jari_jari = jari_jari
    def draw(self):
        print(f"Menggambar lingkaran berwarna {self.warna} dengan panjang jari-jari {self.jari_jari} cm")

class PersegiPanjang(Bentuk):
    def __init__(self, warna, panjang, lebar):
        super().__init__(warna)
        self.panjang = panjang
        self.lebar = lebar
    def draw(self):
        print(f"Menggambar persegi panjang {self.warna} dengan panjang {self.panjang} dan lebar {self.lebar}")

class Factory:
    def buat_bangun_2D(self, jenis_bangun, warna, *args):
        if jenis_bangun == "Lingkaran":
            return Lingkaran(warna, *args)
        elif jenis_bangun == "Persegi Panjang":
            return PersegiPanjang(warna, *args)
        else:
            raise ValueError(f"Tipe bentuk '{jenis_bangun}' tidak valid")

# Contoh penggunaan
factory = Factory()
lingkaran1 = factory.buat_bangun_2D("Lingkaran", "merah", 14)
lingkaran1.draw()
persegi_panjang1 = factory.buat_bangun_2D("Persegi Panjang", "biru", 5, 6)
persegi_panjang1.draw()
