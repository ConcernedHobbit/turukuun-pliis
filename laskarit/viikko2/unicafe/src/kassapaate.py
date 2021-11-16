from maksukortti import Maksukortti

class Kassapaate:
    EDULLISEN_HINTA = 2_40
    MAUKKAAN_HINTA = 4_00

    def __init__(self):
        self.kassassa_rahaa = 1000_00
        self.edulliset = 0
        self.maukkaat = 0

    def kateisella(self, maksu, hinta: int) -> bool:
        if maksu >= hinta:
            self.kassassa_rahaa += hinta
            return True
        return False

    def kortilla(self, kortti: Maksukortti, hinta: int) -> bool:
        return kortti.ota_rahaa(hinta)

    def syo_edullisesti_kateisella(self, maksu):
        if self.kateisella(maksu, self.EDULLISEN_HINTA):
            self.edulliset += 1
            return maksu - self.EDULLISEN_HINTA
        return maksu

    def syo_maukkaasti_kateisella(self, maksu):
        if self.kateisella(maksu, self.MAUKKAAN_HINTA):
            self.maukkaat += 1
            return maksu - self.MAUKKAAN_HINTA
        return maksu

    def syo_edullisesti_kortilla(self, kortti: Maksukortti) -> bool:
        if self.kortilla(kortti, self.EDULLISEN_HINTA):
            self.edulliset += 1
            return True
        return False

    def syo_maukkaasti_kortilla(self, kortti: Maksukortti) -> bool:
        if self.kortilla(kortti, self.MAUKKAAN_HINTA):
            self.maukkaat += 1
            return True
        return False

    def lataa_rahaa_kortille(self, kortti: Maksukortti, summa) -> None:
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return
