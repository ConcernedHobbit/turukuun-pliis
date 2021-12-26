from logic.game import Game
from repository.local import Local
from repository.sheets import Sheets
from service.name_service import NameService
from ui.screen import Screen

if __name__ == '__main__':
    name_service = NameService(
        Local(),
        Sheets()
    )
    game = Game(name_service)
    screen = Screen(game)
    screen.loop()
