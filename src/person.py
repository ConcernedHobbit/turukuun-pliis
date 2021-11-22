from datetime import date
from random import randrange
from typing import Optional
import pygame
import pygame.freetype
from pygame.constants import SRCALPHA


class SSID:
    def __init__(self, birthday: date, individual_number: Optional[int] = None) -> None:
        if 1800 <= birthday.year < 2100:
            self.birthday = birthday
        else:
            raise ValueError(
                'SSID is not defined for years before 1800 or after 2099')

        if individual_number is None:
            self.individual_number = randrange(2, 900)
        else:
            if 2 <= individual_number < 900:
                self.individual_number = individual_number
            else:
                raise ValueError(
                    'SSID individual number should be between 2 and 899 (inclusive)')

    @property
    def _date(self) -> str:
        # date.strftime cannot process years before 1900, so we need to manually format...
        return f'{self.birthday.day:02d}{self.birthday.month:02d}{str(self.birthday.year)[2:]}'

    @property
    def _padded_individual_number(self) -> str:
        return str(self.individual_number).zfill(3)

    @property
    def _niner(self) -> str:
        return f'{self._date}{self._padded_individual_number}'

    @property
    def _checkdigit(self) -> str:
        # https://dvv.fi/en/personal-identity-code
        mod = int(self._niner) % 31
        return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
                'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'][mod]

    @property
    def _seperator(self) -> str:
        century = self.birthday.year // 100

        if century == 18:
            return '+'

        if century == 19:
            return '-'

        # since constructor does not accept invalid years, we can assume that we are in the 20xx
        # will have to be updated once dvv specifices symbol for 21xx
        return 'A'

    def matches_birthyear(self, year: int) -> bool:
        return self.birthday.year == year

    def __repr__(self) -> str:
        return f'{self._date}{self._seperator}{self._padded_individual_number}{self._checkdigit}'


BASE_YEAR = 2020


class Person(pygame.sprite.Sprite):
    def __init__(self, name: Optional[str] = None, age: Optional[int] = None,
                 height: Optional[int] = None, ssid: Optional[SSID] = None) -> None:
        pygame.sprite.Sprite.__init__(self)

        if name is None:
            self.name = 'Matti Meikäläinen'  # TODO: Random generation
        else:
            self.name = name

        if age is None:
            self.age = randrange(12, 80)
        else:
            self.age = age

        if height is None:
            self.height = randrange(150, 220)
        else:
            self.height = height

        if ssid is None:
            # SSID generation based on age
            year = BASE_YEAR - self.age
            month = randrange(8, 13)
            day = randrange(1, 30)
            birthday = date(year, month, day)

            self.ssid = SSID(birthday)
        else:
            self.ssid = ssid

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
