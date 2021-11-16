import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(10_00)
        self.koyha_kortti = Maksukortti(1_00)

    ### Konstruktori
    def test_konstruktori_asettaa_rahamaaran_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000_00)

    def test_konstruktori_asettaa_myydyt_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    ### Rahan lataaminen
    def test_kortille_voi_ladata_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 5_00)
        self.assertEqual(self.kortti.saldo, 10_00 + 5_00)

    def test_kortille_rahan_lataaminen_kasvattaa_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 5_00)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000_00 + 5_00)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -10_00)
        self.assertEqual(self.kortti.saldo, 10_00)

    def test_kortille_negatiivisen_summan_lataaminen_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -10_00)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000_00)

    ### Ostaminen
    ## Edullisen lounaan osto
    # Käteisellä
    def test_kateisella_voi_ostaa_edullisesti(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000_00 + 240)
        self.assertEqual(vaihtoraha, 300 - 240)

    def test_kateisella_osto_kasvattaa_myytyjen_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_riittamattomalla_kateisella_ei_voi_ostaa_edullisesti(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000_00)
        self.assertEqual(vaihtoraha, 100)

    # Kortilla
    def test_kortilla_edullisen_ostaminen_ottaa_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 10_00 - 240)

    def test_kortilla_edullisen_ostaminen_ei_kasvata_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000_00)

    def test_kortilla_osto_kasvattaa_myytyjen_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_edullisen_osto_palauttaa_tosi(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti))

    def test_koyhalla_kortilla_edullisen_ostaminen_ei_ota_rahaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyha_kortti)
        self.assertEqual(self.koyha_kortti.saldo, 1_00)

    def test_koyhalla_kortilla_osto_ei_kasvata_myytyjen_edullisten_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.koyha_kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_koyhalla_kortilla_edullisen_osto_palauttaa_epatosi(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.koyha_kortti))

    ## Maukkaan lounaan osto
    # Käteisellä
    def test_kateisella_voi_ostaa_maukkaasti(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000_00 + 400)
        self.assertEqual(vaihtoraha, 500 - 400)

    def test_kateisella_osto_kasvattaa_myytyjen_maukkaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_riittamattomalla_kateisella_ei_voi_ostaa_maukkaasti(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000_00)
        self.assertEqual(vaihtoraha, 100)

    # Kortilla
    def test_kortilla_maukkaa_ostaminen_ottaa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 10_00 - 400)

    def test_kortilla_maukkaan_ostaminen_ei_kasvata_kassan_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 1000_00)

    def test_kortilla_osto_kasvattaa_myytyjen_maukkaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_maukkaan_osto_palauttaa_tosi(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))

    def test_koyhalla_kortilla_maukkaan_ostaminen_ei_ota_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyha_kortti)
        self.assertEqual(self.koyha_kortti.saldo, 1_00)

    def test_koyhalla_kortilla_osto_ei_kasvata_myytyjen_maukkaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.koyha_kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_koyhalla_kortilla_maukkaan_osto_palauttaa_epatosi(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.koyha_kortti))

    