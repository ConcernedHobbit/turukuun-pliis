from datetime import date, timedelta
import unittest
from logic.entry_documents.entry_document import EntryDocument
from logic.game import Game, State
from logic.person import Person
from logic.player import Player
from logic.checkpoint import Checkpoint
from repository.local import Local
from repository.sheets import Sheets
from service.name_service import NameService

class TestGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._name_service = NameService(
            Local(),
            Sheets()
        )

    def setUp(self):
        self.game = Game(self._name_service)
        self.game.checkpoint.queue.clear()

    def test_initialization(self):
        self.assertIsInstance(self.game.state, State)
        self.assertEqual(self.game.state, State.DAY)
        self.assertIsInstance(self.game.player, Player)
        self.assertIsInstance(self.game.checkpoint, Checkpoint)
        self.assertIsInstance(self.game.day, date)

    def test_tick_when_queue_not_empty(self):
        self.game.checkpoint.populate(1)
        self.game.state = State.DAY
        self.game.tick()
        self.assertEqual(self.game.state, State.DAY)

    def test_tick_when_queue_empty(self):
        self.game.state = State.DAY
        self.game.tick()
        self.assertEqual(self.game.state, State.END_OF_DAY)

    def test_next_day(self):
        current_day = self.game.day
        self.game.state = State.END_OF_DAY
        self.game.next_day()
        self.assertGreater(len(self.game.checkpoint.queue), 0)
        self.assertEqual(self.game.day, current_day + timedelta(days = 1))

    def test_approve_when_queue_empty(self):
        self.game.approve_person()
        self.assertEqual(self.game.player.points, 0)
        self.assertEqual(len(self.game.checkpoint.queue), 0)
        self.assertEqual(len(self.game.checkpoint.processed), 0)

    def test_reject_when_queue_empty(self):
        self.game.reject_person()
        self.assertEqual(self.game.player.points, 0)
        self.assertEqual(len(self.game.checkpoint.queue), 0)
        self.assertEqual(len(self.game.checkpoint.processed), 0)

    def test_approve_when_correct_decision(self):
        self.game.checkpoint.queue.append(Person())
        self.game.approve_person()
        self.assertGreater(self.game.player.points, 0)
        self.assertEqual(len(self.game.checkpoint.queue), 0)
        self.assertEqual(len(self.game.checkpoint.processed), 1)

    def test_approve_when_incorrect_decision(self):
        person = Person()
        person.entry_documents.append(EntryDocument('Passport', False, ''))
        self.game.checkpoint.queue.append(person)
        self.game.approve_person()
        self.assertLess(self.game.player.points, 0)
        self.assertEqual(len(self.game.checkpoint.queue), 0)
        self.assertEqual(len(self.game.checkpoint.processed), 1)

    def test_reject_when_incorrect_decision(self):
        self.game.checkpoint.queue.append(Person())
        self.game.reject_person()
        self.assertLess(self.game.player.points, 0)
        self.assertEqual(len(self.game.checkpoint.queue), 0)
        self.assertEqual(len(self.game.checkpoint.processed), 1)

    def test_reject_when_correct_decision(self):
        person = Person()
        person.entry_documents.append(EntryDocument('Passport', False, ''))
        self.game.checkpoint.queue.append(person)
        self.game.reject_person()
        self.assertGreater(self.game.player.points, 0)
        self.assertEqual(len(self.game.checkpoint.queue), 0)
        self.assertEqual(len(self.game.checkpoint.processed), 1)

    def test_days_passed(self):
        self.game.day += timedelta(days = 10)
        self.assertEqual(self.game.days_passed, 10)

    def test_current_person(self):
        self.assertIsNone(self.game.current_person())
        self.game.checkpoint.queue.append(Person())
        self.assertIsInstance(self.game.current_person(), Person)
