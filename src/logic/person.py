from datetime import date
from random import randrange
from typing import Optional
import pygame
import pygame.freetype
from pygame.constants import SRCALPHA

from logic.ssid import SSID

BASE_YEAR = 2020


# TODO: Seperate sprite logic into an encapsulating class to abstract it away from game logic
class Person(pygame.sprite.Sprite):
    def __init__(self,
                 name: Optional[str] = 'Matti Meikäläinen', # TODO: Random generation
                 age: Optional[int] = randrange(12, 80),
                 height: Optional[int] = randrange(150, 220),
                 ssid: Optional[SSID] = None) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.age = age
        self.height = height

        if ssid is None: # TODO: create SSID.random()
            # SSID generation based on age
            year = BASE_YEAR - self.age
            month = randrange(8, 13)
            day = randrange(1, 30)
            birthday = date(year, month, day)

            self.ssid = SSID(birthday)
        else:
            self.ssid = ssid

        # TODO: seperate sprite into PersonSprite
        # sprite
        self.image = pygame.Surface([150, 300])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()

    def set_image(self, image: pygame.Surface):
        self.image = image
        self.rect = self.image.get_rect()

    def generate_details_surface(self, font: pygame.freetype.Font,
                                 color: Optional[tuple] = (0, 0, 0),
                                 size: Optional[int] = 42) -> pygame.Surface:
        name, _ = font.render(f'{self.name}', fgcolor=color, size=size)
        birthday, _ = font.render(
            f'Born {self.ssid.birthday}', fgcolor=color, size=size)
        ssid, _ = font.render(f'{self.ssid}', fgcolor=color, size=size)
        height, _ = font.render(f'{self.height} cm', fgcolor=color, size=size)

        padding = 10
        lines = [name, birthday, ssid, height]
        width = max(map(lambda surf: surf.get_width(), lines))
        height = sum(map(lambda surf: surf.get_height(), lines)) + \
            len(lines) * padding

        # surface generation
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

        return surface

    def __repr__(self) -> str:
        return f'{self.name} {self.ssid}'
