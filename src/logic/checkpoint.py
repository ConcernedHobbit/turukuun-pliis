from typing import Optional
from logic.person import Person
from logic.player import Player

class Checkpoint:
    """Class for representing a sigle crossing checkpoint.

    Attributes:
        name (str): the name of this checkpoint.
        queue (list): list containing Persons in queue.
        processed (list): list containing Persons that have been processed.
        player (Player): the player assigned to this checkpoint.
    """
    def __init__(self, player: Player) -> None:
        """Initializes Checkpoint.

        Args:
            player (Player): the player assigned to this checkpoint.
        """
        self.name = 'Uusimaa Border Crossing'
        self.queue = []
        self.processed = []

        self.player = player

        self.populate()

    def populate(self, amount: int = 10):
        """Populate the checkpoint's queue with people.

        Args:
            amount (int, optional): amount of people to populate with.
                Defaults to 10.
        """
        for _ in range(amount):
            self.queue.append(Person())

    def current_person(self) -> Optional[Person]:
        """Get current person in queue.

        Returns:
            Optional[Person]: the current person in queue or None if queue is empty.
        """
        if len(self.queue) == 0:
            return None
        return self.queue[-1]

    def next_person(self) -> Optional[Person]:
        """Move the current person into the processed list and
            return the next person in queue.

        Returns:
            Optional[Person]: the next person in queue or None if queue becomes empty.
        """
        if len(self.queue) == 0:
            return None

        self.processed.append(self.queue.pop())
        return self.current_person()
