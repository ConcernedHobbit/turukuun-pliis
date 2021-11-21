import unittest
from person import Person


class TestPerson(unittest.TestCase):
    def test_person_can_be_created(self):
        person = Person('Matti Meikäläinen', 21, 185)

        self.assertEqual(person.name, 'Matti Meikäläinen')
        self.assertEqual(person.age, 21)
        self.assertEqual(person.height, 185)
