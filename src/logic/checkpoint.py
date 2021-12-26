from random import random
from typing import Optional
from logic.entry_documents.passport import Passport
from logic.person import Person

class Checkpoint:
    """Class for representing a sigle crossing checkpoint.

    Attributes:
        name (str): the name of this checkpoint.
        queue (list): list containing Persons in queue.
        processed (list): list containing Persons that have been processed.
        player (Player): the player assigned to this checkpoint.
    """
    def __init__(self, game) -> None:
        """Initializes Checkpoint.

        Args:
            game (Game): the game this checkpoint is in.
        """
        self.name = 'Uusimaa Border Crossing'
        self.queue = []
        self.processed = []

        self.game = game

        self.populate()

    def populate(self,
                 amount: int = 10,
                 fake_percent: int = 0.3):
        """Populate the checkpoint's queue with people.

        Args:
            amount (int, optional): amount of people to populate with.
                Defaults to 10.
            fake_percent (int, optional): amount of people with fake passports.
                Defauls to 0.3 (30%)
        """
        for _ in range(amount):
            person = self.game.person_generator.get_person()
            if random() < (1 - fake_percent):
                passport = Passport(person)
            else:
                passport = Passport.generate_fake(person, self.game.name_service)
            person.entry_documents.append(passport)
            self.queue.append(person)

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
