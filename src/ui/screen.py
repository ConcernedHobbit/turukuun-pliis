from random import choice
import sys
import os
import pygame
import pygame.freetype
from pygame.locals import QUIT
from ui.person_sprite import PersonSprite
from logic.game import Game, State

class ScreenHelper:
    """Static methods for regular operations."""
    @staticmethod
    def centered_text(
        surface: pygame.Surface,
        font: pygame.freetype.Font,
        text: str,
        size: int = 72,
        offsets: tuple = (0, 0)
    ) -> None:
        """Blits centered text on pygame surface

        Args:
            surface (pygame.Surface): the surface to blit onto
            font (pygame.freetype.Font): the font to render with
            text (str): the text to render
            size (int, optional): font size.
                Defaults to 72.
            offsets (tuple, optional): offsets in format(horizontal, vertical).
                Defaults to (0, 0).
        """
        text, rect = font.render(text, size=size)
        rect.center = (
            surface.get_width() / 2 + offsets[0],
            surface.get_height() / 2 + offsets[1]
        )
        surface.blit(
            text,
            rect
        )

class DaySurface:
    """Methods for generating the Day surface."""
    @staticmethod
    def render_last(screen, surface: pygame.Surface, sprite: pygame.sprite.Sprite):
        """Helper method for rendering last processed person on screen.

        Args:
            screen (Screen): the screen in use.
            surface (pygame.Surface): the surface to blit on.
            sprite (pygame.sprite.Sprite): the sprite of the last person.
        """
        screen.font.render_to(surface, (100, 450), 'Last Person', (50, 50, 50))
        surface.blit(
            sprite.generate_details_surface(
                screen.font, color=(125, 125, 125)),
            (100, 500)
        )

    @staticmethod
    def generate(screen) -> pygame.Surface:
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
            f'Checkpoint {screen.game.checkpoint.name}',
            (0, 0, 0)
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

        current = screen.game.checkpoint.current_person()
        if current:
            surface.blit(
                screen.persons.sprites()[0].generate_details_surface(screen.font),
                (100, 200)
            )

        if len(screen.persons.sprites()) > 1:
            DaySurface.render_last(screen, surface, screen.persons.sprites()[1])

        screen.persons.draw(surface)
        return surface

class EndOfDaySurface:
    """Methods for generating the End of Day surface."""
    @staticmethod
    def generate(screen) -> pygame.Surface:
        """Generates the End of Day surface.

        Args:
            screen (Screen): the screen in use.

        Returns:
            pygame.Surface: the End of Day surface to draw on screen.
        """
        surface = pygame.Surface((screen.width, screen.height))
        surface.fill((20, 200, 250))

        ScreenHelper.centered_text(
            surface,
            screen.font,
            'END OF DAY',
            72,
            (0, -50)
        )

        return surface

class MenuSurface:
    """Methods for generating the Menu surface."""
    @staticmethod
    def generate(screen) -> pygame.Surface:
        """Generates the Menu surface.

        Args:
            screen (Screen): the screen in use.

        Returns:
            pygame.Surface: the Menu surface to draw on screen.
        """
        surface = pygame.Surface((screen.width, screen.height))
        surface.fill((150, 175, 250))

        ScreenHelper.centered_text(
            surface,
            screen.font,
            'TURUKUUN PLIIS',
            72,
            (0, -100)
        )

        ScreenHelper.centered_text(
            surface,
            screen.font,
            'PRESS SPACE TO START',
            42
        )

        ScreenHelper.centered_text(
            surface,
            screen.font,
            'PRESS ESC TO QUIT',
            42,
            (0, 30)
        )

        return surface

class Screen:
    """Class for handling game UI.
    Call loop to start the main game loop and display the game.

    Attributes:
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
        self.width = 1920
        self.height = 1080

        pygame.init()
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Turukuun Pliis')
        self.in_menu = True

        self._init_fonts()
        self._init_images()

        # self.checkpoint = Checkpoint()
        self.persons = pygame.sprite.Group()

        first_sprite = PersonSprite(self.game.checkpoint.current_person())
        first_sprite.set_image(self.random_sprite())
        first_sprite.rect.x = 420
        first_sprite.rect.y = 200
        self.persons.add(first_sprite)

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

    def next_person(self) -> None:
        """Move on to the next person in queue.

        To be depreceated.
        """
        next_person = self.game.checkpoint.next_person()

        last_sprite = self.persons.sprites()[0]
        self.persons.empty()

        if next_person:
            last_sprite.rect.y += 300

            next_sprite = PersonSprite(next_person)
            next_sprite.set_image(self.random_sprite())
            next_sprite.rect.x = 420
            next_sprite.rect.y = 200

            self.persons.add(next_sprite)
        self.persons.add(last_sprite)

    def _handle_events(self):
        """Handle pygame events."""
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if self.in_menu:
                    if event.key == pygame.K_SPACE:
                        self.in_menu = False

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

                if not self.in_menu:
                    if event.key == pygame.K_ESCAPE:
                        self.in_menu = True

                    if event.key in (pygame.K_y, pygame.K_n):
                        self.next_person()
                        self.game.tick()

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
