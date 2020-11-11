class Arac_Alis:
    ana_renkler = ['siyah', 'beyaz', 'gri']

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
        return {'model': self.model, 'satis fiyati': self.satis_fiyati, 'alis fiyati': self.alis_fiyati, 'renk': self.renk, 'cip no': self.cip_no()}

    def calinti_mi(self):
        return self.cip_no() >= 20


# Geçerli ve geçersiz nesneler
# Geçerli
valid_arac = Arac_Alis(2007, "Kırmızı", 8000, 20000,
                       22000, True, True, "AbCdEfGhIj12345")

# Model yılı 2006-2017 arasında değil
valid_arac1 = Arac_Alis(1999, "Kırmızı", 8000, 20000,
                        22000, True, True, "AbCdEfGhIj12345")

# Renk ana renkler dışında değil
valid_arac2 = Arac_Alis(2007, "Beyaz", 8000, 20000,
                        22000, True, True, "AbCdEfGhIj12345")

# Masraf 25.000 liranın altında değil
valid_arac3 = Arac_Alis(2007, "Kırmızı", 30000, 20000,
                        22000, True, True, "AbCdEfGhIj12345")

# Satış fiyatı 15.000 liranın üstünde değil
valid_arac4 = Arac_Alis(2007, "Kırmızı", 8000, 20000,
                        14000, True, True, "AbCdEfGhIj12345")

# Yedek anahtarı yok
valid_arac5 = Arac_Alis(2007, "Kırmızı", 8000, 20000,
                        22000, False, True, "AbCdEfGhIj12345")

# Muayene ve egzoz bakımı yapılmamış
valid_arac6 = Arac_Alis(2007, "Kırmızı", 8000, 20000,
                        22000, True, False, "AbCdEfGhIj12345")

# Şifre 15 karakterden oluşmuyor
valid_arac7 = Arac_Alis(2007, "Kırmızı", 8000, 20000,
                        22000, True, True, "CdEfGhIj123")

# Şifrenin ilk 10 karakteri büyük-küçük harflerden oluşmuyor
valid_arac8 = Arac_Alis(2007, "Kırmızı", 8000, 20000,
                        22000, True, True, "abcdefgh12345")

# Şifrenin son 5 karakteri rakamlardan oluşmuyor
valid_arac8 = Arac_Alis(2007, "Kırmızı", 8000, 20000,
                        22000, True, True, "abcdefgh123tr")


class Arac_Kayit:
    def __init__(self, model, satis, alis, renk, cip_no):
        self.model = model
        self.satis = satis
        self.alis = alis
        self.renk = renk
        self.cip_no = cip_no


# Araç kayıt ile ilgili geçerli ve geçersiz nesneler
# Geçerli
valid_kayit = Arac_Kayit(valid_arac.model, valid_arac.satis_fiyati,
                         valid_arac.alis_fiyati, valid_arac.renk, valid_arac.cip_no())
# ilk değer model yili değil
valid_kayit1 = Arac_Kayit(valid_arac.masraf, valid_arac.satis_fiyati,
                          valid_arac.alis_fiyati, valid_arac.renk, valid_arac.cip_no())
# Son değerde çip numarası yerine çipin kendisi alınmış
valid_kayit2 = Arac_Kayit(valid_arac.model, valid_arac.satis_fiyati,
                          valid_arac.alis_fiyati, valid_arac.renk, valid_arac.cip)
# İkinci değer satış fiyatı değil
valid_kayit3 = Arac_Kayit(valid_arac.model, valid_arac.yedek_anahtar,
                          valid_arac.alis_fiyati, valid_arac.renk, valid_arac.cip_no())
# Uçüncü değer alış fiyatı değil
valid_kayit4 = Arac_Kayit(valid_arac.model, valid_arac.satis_fiyati,
                          valid_arac.calinti_mi(), valid_arac.renk, valid_arac.cip_no())
