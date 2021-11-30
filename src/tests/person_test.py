import unittest
from datetime import date
from logic.person import Person, SSID


class TestPerson(unittest.TestCase):
    def test_person_can_be_created(self):
        ssid = SSID(date(2000, 12, 20))
        person = Person('Matti Meikäläinen', 21, 185, ssid)

        self.assertEqual(person.name, 'Matti Meikäläinen')
        self.assertEqual(person.age, 21)
        self.assertEqual(person.height, 185)
        self.assertEqual(ssid, person.ssid)

    def test_person_can_be_randomized(self):
        person = Person()

        self.assertIsInstance(person.name, str)

        self.assertGreater(person.age, 0)
        self.assertLess(person.age, 125)

        self.assertGreater(person.height, 100)
        self.assertLess(person.height, 250)

        self.assertIsInstance(person.ssid, SSID)
