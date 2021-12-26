import unittest
from datetime import date
from logic.person import Person
from logic.ssid import SSID
from logic.entry_documents.entry_document import EntryDocument


class TestPerson(unittest.TestCase):
    def test_person_can_be_created(self):
        ssid = SSID(date(2000, 12, 20))
        entry_documents = [EntryDocument('Test')]
        person = Person('Matti Meikäläinen', 21, 185, ssid, entry_documents)

        self.assertEqual(person.name, 'Matti Meikäläinen')
        self.assertEqual(person.age, 21)
        self.assertEqual(person.height, 185)
        self.assertEqual(person.ssid, ssid)
        self.assertEqual(person.entry_documents, entry_documents)

    def test_person_can_be_randomized(self):
        person = Person()

        self.assertIsInstance(person.name, str)

        self.assertGreater(person.age, 0)
        self.assertLess(person.age, 125)

        self.assertGreater(person.height, 100)
        self.assertLess(person.height, 250)

        self.assertIsInstance(person.ssid, SSID)

        self.assertEqual(len(person.entry_documents), 0)

    def test_string_representation(self):
        ssid = SSID(date(2000, 12, 20))
        person = Person('Matti Meikäläinen', 21, 185, ssid)

        ssid_repr = str(ssid)
        person_repr = str(person)

        self.assertIn('Matti Meikäläinen', person_repr)
        self.assertIn(ssid_repr, person_repr)

    def test_get_entry_document(self):
        person = Person()
        self.assertIsNone(person.get_entry_document('Test'))

        entry_document = EntryDocument('Test')
        person.entry_documents.append(entry_document)
        self.assertEqual(person.get_entry_document('Test'), entry_document)

    def test_has_entry_document(self):
        person = Person()
        self.assertFalse(person.has_entry_document('Test'))

        entry_document = EntryDocument('Test')
        person.entry_documents.append(entry_document)
        self.assertTrue(person.has_entry_document('Test'))
