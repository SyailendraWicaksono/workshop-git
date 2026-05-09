import unittest

# Fungsi yang akan diuji
def hitung_luas(panjang, lebar):
    return panjang * lebar


# Unit Test
class TestHitungLuas(unittest.TestCase):

    def test_luas_positif(self):
        self.assertEqual(hitung_luas(10, 5), 50)

    def test_luas_desimal(self):
        self.assertEqual(hitung_luas(2.5, 4), 10.0)

    def test_luas_nol(self):
        self.assertEqual(hitung_luas(0, 5), 0)


# Menjalankan test
if __name__ == "__main__":
    unittest.main()