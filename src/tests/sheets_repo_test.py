import unittest

from repository.sheets import Sheets

class SheetsRepoTest(unittest.TestCase):
    def setUp(self):
        self.sheets = Sheets()

    def test_get_column_as_list(self):
        self.assertListEqual(
            self.sheets.get_column_as_list('test', 'alpha'),
            ['one', 'two', 'three']
        )
        self.assertListEqual(
            self.sheets.get_column_as_list('test', 'beta'),
            ['four', 'five', 'six']
        )
        self.assertListEqual(
            self.sheets.get_column_as_list('test', 'gamma'),
            ['seven', 'eight', 'nine']
        )

    def is_long(self, names):
        self.assertGreater(
            len(names),
            1000
        )

    def test_get_male_first_names(self):
        self.is_long(self.sheets.get_male_first_names())

    def test_get_female_first_names(self):
        self.is_long(self.sheets.get_female_first_names())

    def test_get_surnames(self):
        self.is_long(self.sheets.get_surnames())
