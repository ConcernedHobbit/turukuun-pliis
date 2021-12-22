from typing import Optional
from logic.person import Person

class Checkpoint:
    def __init__(self):
        self.name = 'Uusimaa Border Crossing'
        self.queue = []
        self.processed = []

        self._populate()

    def _populate(self, amount: int = 10):
        for _ in range(amount):
            self.queue.append(Person())

    def current_person(self) -> Optional[Person]:
        if len(self.queue) == 0:
            return None
        return self.queue[-1]

    def next_person(self) -> Optional[Person]:
        if len(self.queue) == 0:
            return None

        self.processed.append(self.queue.pop())
        return self.current_person()
