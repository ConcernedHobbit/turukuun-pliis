import unittest
from logic.entry_documents.entry_document import EntryDocument

class TestEntryDocument(unittest.TestCase):
    def setUp(self):
        self.entry_document = EntryDocument('Test')

    def test_initialization(self):
        self.assertIsInstance(self.entry_document.name, str)
        self.assertTrue(self.entry_document.valid)
        self.assertIsNone(self.entry_document.reason_not_valid)
