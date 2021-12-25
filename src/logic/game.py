from enum import Enum, auto
from datetime import date, timedelta
from logic.checkpoint import Checkpoint
from logic.player import Player

# docstrining enums is complicated[1] and values are self-explanatory.
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
        """Initializes Game.
        """
        # TODO: Load data from savefile
        self.state = State.DAY
        self.player = Player()
        self.checkpoint = Checkpoint(self.player)
        self.day = date(2020, 3, 20)

    def tick(self) -> None:
        """Advance game logic.
        Has to be called after player takes any action.
        """
        if self.state is State.DAY and len(self.checkpoint.queue) == 0:
            self.state = State.END_OF_DAY

    def next_day(self) -> None:
        """Progress to the next day.
        Should only be called from the end of day report.
        """
        assert self.state is State.END_OF_DAY, 'Day can only be advanced after End of Day'
        self.checkpoint.populate()
        self.day = self.day + timedelta(days = 1)
