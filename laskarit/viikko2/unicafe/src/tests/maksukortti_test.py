import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_kortilta_voi_ottaa_rahaa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_kortilta_liikaa_ottaminen_ei_vahenna_saldoa(self):
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_kortilta_ottaminen_palauttaa_tosi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))

    def test_kortilta_liikaa_ottaminen_palauttaa_epatosi(self):
        self.assertFalse(self.maksukortti.ota_rahaa(15))

    def test_kortin_tulostus_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")