from logic.game import Game
from ui.screen import Screen

if __name__ == '__main__':
    game = Game()
    screen = Screen(game)
    screen.loop()
