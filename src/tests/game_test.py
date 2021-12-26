from datetime import date, timedelta
import unittest
from logic.game import Game, State
from logic.player import Player
from logic.checkpoint import Checkpoint

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initialization(self):
        self.assertIsInstance(self.game.state, State)
        self.assertEqual(self.game.state, State.DAY)
        self.assertIsInstance(self.game.player, Player)
        self.assertIsInstance(self.game.checkpoint, Checkpoint)
        self.assertIsInstance(self.game.day, date)

    def test_tick_when_queue_not_empty(self):
        self.game.checkpoint.queue.clear()
        self.game.checkpoint.populate(1)
        self.game.state = State.DAY
        self.game.tick()
        self.assertEqual(self.game.state, State.DAY)

    def test_tick_when_queue_empty(self):
        self.game.checkpoint.queue.clear()
        self.game.state = State.DAY
        self.game.tick()
        self.assertEqual(self.game.state, State.END_OF_DAY)

    def test_next_day(self):
        current_day = self.game.day
        self.game.checkpoint.queue.clear()
        self.game.state = State.END_OF_DAY
        self.game.next_day()
        self.assertGreater(len(self.game.checkpoint.queue), 0)
        self.assertEqual(self.game.day, current_day + timedelta(days = 1))
