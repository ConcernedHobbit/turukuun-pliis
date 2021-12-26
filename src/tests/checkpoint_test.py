import unittest
from logic.checkpoint import Checkpoint
from logic.player import Player
from logic.person import Person

class TestCheckpoint(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.checkpoint = Checkpoint(self.player)

    def only_people_in_queue(self):
        # All people in the queue are instances of Person
        for value in self.checkpoint.queue:
            self.assertIsInstance(value, Person)

    def test_initialization(self):
        self.assertIsInstance(self.checkpoint.name, str)
        self.assertIsInstance(self.checkpoint.queue, list)
        self.assertIsInstance(self.checkpoint.processed, list)
        self.assertIsInstance(self.checkpoint.player, Player)

    def test_populated_at_start(self):
        self.assertGreater(len(self.checkpoint.queue), 0)

    def test_no_processed_at_start(self):
        self.assertEqual(len(self.checkpoint.processed), 0)

    def test_populate_default(self):
        self.checkpoint.queue.clear()
        self.checkpoint.populate()
        self.assertEqual(len(self.checkpoint.queue), 10)
        self.only_people_in_queue()

    def test_populate(self):
        self.checkpoint.queue.clear()
        self.checkpoint.populate(20)
        self.assertEqual(len(self.checkpoint.queue), 20)
        self.only_people_in_queue()

    def test_populate_without_clearing(self):
        amount = len(self.checkpoint.queue)
        self.checkpoint.populate(5)
        self.assertEqual(len(self.checkpoint.queue), amount + 5)
        self.only_people_in_queue()

    def test_current_person(self):
        self.assertIsInstance(self.checkpoint.current_person(), Person)

        # Empty queue returns None
        self.checkpoint.queue.clear()
        self.assertIsNone(self.checkpoint.current_person())

    def test_next_person(self):
        next_person = self.checkpoint.next_person()
        self.assertIsInstance(next_person, Person)

        # Previous person goes to processed list
        self.assertEqual(len(self.checkpoint.processed), 1)
        self.assertIsInstance(self.checkpoint.processed[0], Person)

        # Person changes
        self.assertNotEqual(next_person, self.checkpoint.next_person())

        # Empty queue returns None
        self.checkpoint.queue.clear()
        self.assertIsNone(self.checkpoint.next_person())

        # Only one person in queue returns None
        self.checkpoint.queue.append(Person())
        self.assertIsNone(self.checkpoint.next_person())
