class Galeri:
    def __init__(self, model, renk, masraf, alis_fiyati, satis_fiyati, muayene, yedek_anahtar, cip):
        self.model = model
        self.renk = renk
        self.masraf = masraf
        self.satis_fiyati = satis_fiyati
        self.alis_fiyati = alis_fiyati
        self.muayene = muayene
        self.yedek_anahtar = yedek_anahtar
        self.cip = cip

    def cip_no(self):
        no = 0
        for i in self.cip:
            if i.isdigit():
                no += int(i)

        return no

    def satis(self):
        return [self.model, self.satis_fiyati, self.alis_fiyati, self.renk, self.cip_no()]

    def calinti_mi(self):
        return self.cip_no() >= 20


gl = Galeri(2007, "Gri", 8000, 20000, 22000, True, True, "AbCdEfGhIj12345")

print(gl.calinti_mi())
