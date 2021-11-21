import unittest
from datetime import date
from person import SSID


class TestSSID(unittest.TestCase):
    def test_1800s(self):
        ids = [
            # minimum individual number with min. date, arbitrary middle date, max. date
            SSID(date(1800, 1, 1), 2),
            SSID(date(1850, 6, 16), 2),
            SSID(date(1899, 12, 31), 2),

            # arbitrary individual number with min. date, arbitrary middle date, max. date
            SSID(date(1800, 1, 1), 123),
            SSID(date(1850, 6, 16), 123),
            SSID(date(1899, 12, 31), 123),

            # maximum individual number with min. date, arbitrary middle date, max. date
            SSID(date(1800, 1, 1), 899),
            SSID(date(1850, 6, 16), 899),
            SSID(date(1899, 12, 31), 899)
        ]

        expected_results = [
            '010100+002H',
            '160650+0024',
            '311299+0029',

            '010100+123D',
            '160650+1231',
            '311299+1236',

            '010100+899E',
            '160650+8992',
            '311299+8997'
        ]

        for ssid, expected_result in zip(ids, expected_results):
            self.assertEqual(str(ssid), expected_result)

    def test_1900s(self):
        ids = [
            # minimum individual number with min. date, arbitrary middle date, max. date
            SSID(date(1900, 1, 1), 2),
            SSID(date(1950, 6, 16), 2),
            SSID(date(1999, 12, 31), 2),

            # arbitrary individual number with min. date, arbitrary middle date, max. date
            SSID(date(1900, 1, 1), 123),
            SSID(date(1950, 6, 16), 123),
            SSID(date(1999, 12, 31), 123),

            # maximum individual number with min. date, arbitrary middle date, max. date
            SSID(date(1900, 1, 1), 899),
            SSID(date(1950, 6, 16), 899),
            SSID(date(1999, 12, 31), 899)
        ]

        expected_results = [
            '010100-002H',
            '160650-0024',
            '311299-0029',

            '010100-123D',
            '160650-1231',
            '311299-1236',

            '010100-899E',
            '160650-8992',
            '311299-8997'
        ]

        for ssid, expected_result in zip(ids, expected_results):
            self.assertEqual(str(ssid), expected_result)

    def test_2000s(self):
        ids = [
            # minimum individual number with min. date, arbitrary middle date, max. date
            SSID(date(2000, 1, 1), 2),
            SSID(date(2050, 6, 16), 2),
            SSID(date(2099, 12, 31), 2),

            # arbitrary individual number with min. date, arbitrary middle date, max. date
            SSID(date(2000, 1, 1), 123),
            SSID(date(2050, 6, 16), 123),
            SSID(date(2099, 12, 31), 123),

            # maximum individual number with min. date, arbitrary middle date, max. date
            SSID(date(2000, 1, 1), 899),
            SSID(date(2050, 6, 16), 899),
            SSID(date(2099, 12, 31), 899)
        ]

        expected_results = [
            '010100A002H',
            '160650A0024',
            '311299A0029',

            '010100A123D',
            '160650A1231',
            '311299A1236',

            '010100A899E',
            '160650A8992',
            '311299A8997'
        ]

        for ssid, expected_result in zip(ids, expected_results):
            self.assertEqual(str(ssid), expected_result)

    def test_1700s_raises_error(self):
        with self.assertRaises(ValueError):
            SSID(date(1700, 1, 1))

    def test_2100s_raises_error(self):
        with self.assertRaises(ValueError):
            SSID(date(2100, 1, 1))

    def test_individual_number_below_2_raises_error(self):
        with self.assertRaises(ValueError):
            SSID(date(2000, 12, 20), 1)

    def test_individual_number_above_899_raises_error(self):
        with self.assertRaises(ValueError):
            SSID(date(2000, 12, 20), 900)

    def test_ssid_with_no_individual_number_gets_assigned_random_one(self):
        ssid = SSID(date(2000, 12, 20))
        self.assertGreaterEqual(ssid.individual_number, 2)
        self.assertLessEqual(ssid.individual_number, 899)
