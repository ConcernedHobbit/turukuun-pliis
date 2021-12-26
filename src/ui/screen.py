from __future__ import annotations
from random import choice
import sys
import os

import pygame
import pygame.freetype
from pygame.locals import QUIT

from ui.helper import Helper
from ui.passport_sprite import PassportSprite
from ui.person_sprite import PersonSprite
from logic.game import Game, State

class DaySurface:
    """Methods for generating the Day surface."""
    @staticmethod
    def generate(screen: Screen) -> pygame.Surface:
        """Generates the Day surface.

        Args:
            screen (Screen): the screen in use.

        Returns:
            pygame.Surface: the Day surface to draw onto the screen.
        """
        surface = pygame.Surface((screen.width, screen.height))

        surface.fill((150, 175, 250))
        screen.font.render_to(
            surface,
            (10, 10),
            f'{screen.game.checkpoint.name} | Day {screen.game.day}',
            (0, 0, 0),
            size = 50
        )

        screen.font.render_to(
            surface,
            (10, 60),
            'Objective:',
            (0, 0, 0)
        )
        screen.font.render_to(
            surface,
            (10, 100),
            '- Check that details match',
            (0, 0, 0)
        )

        screen.font.render_to(
            surface,
            (10, 140),
            f'In Queue: {len(screen.game.checkpoint.queue)}',
            (0, 100, 0)
        )

        current = screen.game.checkpoint.current_person()
        if current:
            surface.blit(
                current.sprite.generate_details_surface(screen.font),
                (100, 200)
            )
            surface.blit(
                current.sprite.image,
                (470, 250)
            )
            if current.has_entry_document('Passport'):
                surface.blit(
                    PassportSprite(
                        current.get_entry_document('Passport'),
                        screen.font
                    ).image,
                    (600, 200)
            )

        return surface

class EndOfDaySurface:
    """Methods for generating the End of Day surface."""
    @staticmethod
    def generate(screen: Screen) -> pygame.Surface:
        """Generates the End of Day surface.

        Args:
            screen (Screen): the screen in use.

        Returns:
            pygame.Surface: the End of Day surface to draw on screen.
        """
        surface = pygame.Surface((screen.width, screen.height))
        surface.fill((20, 200, 250))

        Helper.centered_text(
            surface,
            screen.font,
            'END OF DAY',
            72,
            (0, -50)
        )

        Helper.centered_text(
            surface,
            screen.font,
            f'Points: {screen.game.player.points}'
        )

        Helper.centered_text(
            surface,
            screen.font,
            'PRESS SPACE FOR NEXT DAY',
            50,
            (0, 30)
        )

        surface.blit(
            Helper.multiline_text(
                screen.font,
                Helper.point_explanation(screen.game),
                30
            ),
            (100, 500)
        )

        return surface

class MenuSurface:
    """Methods for generating the Menu surface."""
    @staticmethod
    def generate(screen: Screen) -> pygame.Surface:
        """Generates the Menu surface.

        Args:
            screen (Screen): the screen in use.

        Returns:
            pygame.Surface: the Menu surface to draw on screen.
        """
        surface = pygame.Surface((screen.width, screen.height))
        surface.fill((150, 175, 250))

        Helper.centered_text(
            surface,
            screen.font,
            'TURUKUUN PLIIS',
            120,
            (0, -200)
        )

        Helper.centered_text(
            surface,
            screen.font,
            'PRESS SPACE TO START',
            offsets = (0, -100)
        )

        Helper.centered_text(
            surface,
            screen.font,
            'PRESS Q TO QUIT',
            offsets = (0, -70)
        )

        surface.blit(
            Helper.multiline_text(
                screen.font,
                Helper.point_explanation(screen.game),
                30
            ),
            (100, 500)
        )

        return surface

class Screen:
    """Class for handling game UI.
    Call loop to start the main game loop and display the game.

    Attributes:
        game (Game): the game instance.
        fps (int): frames per second to display.
        width (int): width of the screen.
        height (int): height of the screen.
        clock (pygame.time.Clock): internal pygame clock.
        window (pygame.Surface): the main window.
        persons (pygame.sprite.Group): list containing sprites to draw.
            To be depreceated.
        person_sprites (list): list containing pygame Surfaces
            representing peoples' pictures
        font (pygame.freetype.Font): the main font.
    """
    def __init__(self, game: Game):
        """Initializes Screen.

        Args:
            game (Game): the Game instance to use.
        """
        self.game = game

        self.fps = 60
        self.height = 720
        self.width = 1080

        self.custom_events = {
            'NEXT_DAY': pygame.USEREVENT + 1,
            'REJECT_PERSON': pygame.USEREVENT + 2,
            'APPROVE_PERSON': pygame.USEREVENT + 3
        }

        pygame.init()
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Turukuun Pliis')
        self.in_menu = True

        self._init_fonts()
        self._init_images()
        self.apply_sprites()

    def _init_fonts(self) -> None:
        """Initialize fonts."""
        font_directory = os.path.join('data', 'fonts')
        self.font = pygame.freetype.Font(os.path.join(
            font_directory, 'VT323-Regular.ttf'), 42)

    def _init_images(self) -> None:
        """Initialize all images."""
        image_directory = os.path.join('data', 'sprites')
        self.person_sprites = []

        # TODO: Dynamic loading?
        for filename in ('person.png', 'person2.png', 'person3.png'):
            sprite = pygame.image.load(
                os.path.join(image_directory, filename)
            )
            self.person_sprites.append(sprite)

    def tick(self) -> None:
        """Method for handling ticks happening every frame."""
        pygame.display.update()
        self.clock.tick(self.fps)

    def random_sprite(self) -> pygame.Surface:
        """Get a random avatar sprite.

        Returns:
            pygame.Surface: a random image.
        """
        return choice(self.person_sprites)

    def apply_sprites(self) -> None:
        """Apply a PersonSprite to every person in queue."""
        for person in self.game.checkpoint.queue:
            person.sprite = PersonSprite(person)
            person.sprite.set_image(self.random_sprite())

    def _handle_events(self):
        """Handle pygame events."""
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if self.in_menu:
                    if event.key in (pygame.K_SPACE, pygame.K_ESCAPE):
                        self.in_menu = False

                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

                elif self.game.state == State.END_OF_DAY:
                    if event.key == pygame.K_ESCAPE:
                        self.in_menu = True

                    if event.key == pygame.K_SPACE:
                        self.game.next_day()
                        self.apply_sprites()

                elif self.game.state == State.DAY:
                    if event.key == pygame.K_ESCAPE:
                        self.in_menu = True

                    if event.key == pygame.K_y:
                        self.game.approve_person()
                        self.game.tick()

                    if event.key == pygame.K_n:
                        self.game.reject_person()
                        self.game.tick()

                else:
                    # In an incorrect state, any key press will quit.
                    pygame.quit()
                    sys.exit()

            if event.type == self.custom_events['NEXT_DAY']:
                if self.game.state == State.END_OF_DAY:
                    self.game.next_day()
                    self.apply_sprites()

            if event.type == self.custom_events['REJECT_PERSON']:
                if self.game.state == State.DAY:
                    self.game.reject_person()

            if event.type == self.custom_events['APPROVE_PERSON']:
                if self.game.state == State.DAY:
                    self.game.approve_person()

    def loop(self):
        """Main loop, call to start the screen."""
        while True:
            self._handle_events()

            if self.in_menu:
                self.window.blit(MenuSurface.generate(self), (0, 0))
            elif self.game.state is State.DAY:
                self.window.blit(DaySurface.generate(self), (0, 0))
            elif self.game.state is State.END_OF_DAY:
                self.window.blit(EndOfDaySurface.generate(self), (0, 0))
            self.tick()
