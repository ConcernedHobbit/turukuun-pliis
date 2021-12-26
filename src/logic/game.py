from enum import Enum, auto
from datetime import date, timedelta
from math import floor, sqrt
from random import randrange
from typing import Optional
from logic.checkpoint import Checkpoint
from logic.person import Person
from logic.player import Player

# docstringing enums is complicated[1] and values are self-explanatory.
# [1] https://stackoverflow.com/a/50475245
class State(Enum):
    DAY = auto()
    END_OF_DAY = auto()

class Game:
    """Class for handling a single instance of the game

    Attributes:
        state (State): the State of the game.
        player (Player): the Player playing the game.
        checkpoint (Checkpoint): the current checkpoint.
        day (date): the current in-game date.
    """
    def __init__(self) -> None:
        """Initializes Game."""
        # TODO: Load data from savefile
        self.state = State.DAY
        self.player = Player()
        self.checkpoint = Checkpoint(self.player)

        self.start_date = date(2020, 3, 20)
        self.day = self.start_date

        self.points_for_correct_approval = 25
        self.points_for_incorrect_approval = -100
        self.points_for_correct_rejection = 100
        self.points_for_incorrect_rejection = -200

    def tick(self) -> None:
        """Advance game logic.
        Has to be called after player takes any action."""
        if self.state is State.DAY and len(self.checkpoint.queue) == 0:
            self.state = State.END_OF_DAY

    def approve_person(self) -> None:
        """Approve the current person to pass.
        Will process the current person, so they are removed from the queue."""
        person = self.checkpoint.current_person()
        if not person:
            return

        if all(document.valid for document in person.entry_documents):
            self.player.points += self.points_for_correct_approval
        else:
            self.player.points += self.points_for_incorrect_approval

        self.checkpoint.next_person()

    def reject_person(self) -> None:
        """Reject the current person from passing.
        Will process the current person, so they are removed from the queue."""
        person = self.checkpoint.current_person()
        if not person:
            return

        if all(document.valid for document in person.entry_documents):
            self.player.points += self.points_for_incorrect_rejection
        else:
            self.player.points += self.points_for_correct_rejection

        self.checkpoint.next_person()

    def current_person(self) -> Optional[Person]:
        """Returns the current person from the current checkpoint.

        Returns:
            Optional[Person]: the current person or None if queue is empty.
        """
        return self.checkpoint.current_person()

    @property
    def days_passed(self) -> int:
        return (self.day - self.start_date).days

    def next_day(self) -> None:
        """Progress to the next day.
        Should only be called from the end of day report."""
        assert self.state is State.END_OF_DAY, 'Day can only be advanced after End of Day'

        self.day = self.day + timedelta(days = 1)

        self.checkpoint.populate(
            randrange(
                floor(10 * sqrt(self.days_passed)),
                floor(20 * sqrt(self.days_passed)),
            ),
            # Minimum fake percentage: 30%. Approaches maximum of 80% linearly over 60 days.
            # TODO: Magic numbers begone.
            0.3 + min(self.days_passed / 60, 0.5)
        )

        self.points_for_correct_approval = floor(self.points_for_correct_approval * 0.95)
        self.points_for_correct_rejection = floor(self.points_for_correct_rejection * 0.97)
        self.points_for_incorrect_approval = floor(self.points_for_incorrect_approval * 1.05)
        self.points_for_incorrect_rejection = floor(self.points_for_incorrect_rejection * 1.07)

        self.state = State.DAY
