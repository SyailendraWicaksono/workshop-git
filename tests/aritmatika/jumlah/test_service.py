import unittest

from src.aritmatika.jumlah.service import jumlah


class TestJumlah(unittest.TestCase):
    def test_tambah_angka_positif(self):
        hasil = jumlah(10, 5)
        self.assertEqual(hasil, 15)

    def test_tambah_angka_negatif(self):
        hasil = jumlah(-3, -7)
        self.assertEqual(hasil, -10)

    def test_tambah_angka_positif_dan_negatif(self):
        hasil = jumlah(10, -3)
        self.assertEqual(hasil, 7)

    def test_tambah_dengan_nol(self):
        hasil = jumlah(8, 0)
        self.assertEqual(hasil, 8)
