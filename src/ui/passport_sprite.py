import pygame

import pygame.freetype
from pygame.constants import SRCALPHA
from logic.entry_documents.passport import Passport

class PassportSprite(pygame.sprite.Sprite):
    """Sprite representation of Passport."""
    def __init__(self, passport: Passport, font: pygame.freetype.Font) -> None:
        """Initializes PassportSprite.

        Args:
            passport: the passport this sprite represents.
            font: the font used to render the passport.
        """
        pygame.sprite.Sprite.__init__(self)
        self.passport = passport
        self.font = font

        self.image = self._generate_surface()
        self.rect = self.image.get_rect()

    def _generate_title(self, name):
        title, _ = self.font.render(
            f'{name}',
            fgcolor = (100, 100, 100),
            size = 28
        )
        return title

    def _generate_detail(self, detail):
        detail, _ = self.font.render(
            f'{detail}',
            fgcolor = (0, 0, 0)
        )
        return detail

    def _generate_surface(self) -> pygame.Surface:
        title, _ = self.font.render(
            'Passi | Pass | Passport',
            fgcolor = (0, 0, 0),
            size = 50
        )

        padding = 10
        lines = [
            title,
            self._generate_title('LAST NAME'),
            self._generate_detail(self.passport.details.name.split()[1]),
            self._generate_title('FIRST NAME'),
            self._generate_detail(self.passport.details.name.split()[0]),
            self._generate_title('SSID'),
            self._generate_detail(self.passport.details.ssid)
        ]
        width = max(map(lambda surf: surf.get_width(), lines))
        height = sum(map(lambda surf: surf.get_height(), lines)) + \
            len(lines) * padding

        background = pygame.Surface((width, height))
        background.fill((120, 110, 80))

        surface = pygame.Surface(
            (
                width,
                height
            ),
            SRCALPHA
        )

        current_height = 0
        for line in lines:
            surface.blit(
                line,
                (
                    0,
                    current_height
                )
            )

            current_height += line.get_height()
            current_height += padding

        background.blit(surface, (0, 0))
        return surface
