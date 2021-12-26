from datetime import date
import unittest
from logic.entry_documents.passport import Passport
from logic.person import Person, PersonDetails
from logic.ssid import SSID
from repository.local import Local
from repository.sheets import Sheets
from service.name_service import NameService

class TestEntryDocument(unittest.TestCase):
    def setUp(self):
        self.person = Person(
            'Testi Keissi',
            20,
            170,
            SSID(
                date(2020, 10, 10),
                500
            )
        )

    def test_initialization(self):
        passport = Passport(self.person)
        self.assertEqual(passport.person, self.person)
        self.assertEqual(passport.details, self.person.details)
        self.assertTrue(passport.valid)
        self.assertIsNone(passport.reason_not_valid)

    def test_manual_fake_generation(self):
        fake_details = [
            PersonDetails(
                'Feikki Keissi',
                self.person.age,
                self.person.height,
                self.person.ssid
            ),
            PersonDetails(
                self.person.name,
                50,
                self.person.height,
                self.person.ssid
            ),
            PersonDetails(
                self.person.name,
                self.person.age,
                230,
                self.person.ssid
            ),
            PersonDetails(
                self.person.name,
                self.person.age,
                self.person.height,
                SSID(
                    date(2020, 11, 11),
                    500
                )
            )
        ]

        wrong_detail = ['name', 'age', 'height', 'ssid']

        for details, wrong in zip(fake_details, wrong_detail):
            fake_passport = Passport(self.person, details)
            self.assertEqual(fake_passport.person, self.person)
            self.assertNotEqual(fake_passport.details, self.person.details)
            self.assertFalse(fake_passport.valid)
            self.assertIn(
                wrong.lower(),
                fake_passport.reason_not_valid.lower()
            )

    def test_fake_generation(self):
        name_service = NameService(
            Local(),
            Sheets()
        )
        fake_passport = Passport.generate_fake(self.person, name_service)
        self.assertEqual(fake_passport.person, self.person)
        self.assertNotEqual(fake_passport.details, self.person.details)
        self.assertFalse(fake_passport.valid)
        self.assertIsInstance(fake_passport.reason_not_valid, str)
