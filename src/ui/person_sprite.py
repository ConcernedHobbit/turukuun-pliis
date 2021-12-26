from typing import Optional
import pygame

import pygame.freetype
from pygame.constants import SRCALPHA
from logic.person import Person

class PersonSprite(pygame.sprite.Sprite):
    """Sprite representation of Person.

    Attributes:
        person (Person): the person this sprite represents.
        image (pygame.Surface): the image of this person.
        rect (pgame.Rect): the rectangle covering image.
    """
    def __init__(self, person: Person) -> None:
        """Initializes PersonSprite.

        Args:
            person (Person): the person this sprite represents.
        """
        pygame.sprite.Sprite.__init__(self)
        self.person = person

        self.image = pygame.Surface([150, 300])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()

    def set_image(self, image: pygame.Surface) -> None:
        """Sets the image for this Person's pygame surface.

        Args:
            image (pygame.Surface): The image to be set
        """
        self.image = image
        self.rect = self.image.get_rect()

    # NOTE: Consider splitting into own class? If person details are constant
    def generate_details_surface(self, font: pygame.freetype.Font,
                                 color: Optional[tuple] = (0, 0, 0),
                                 font_size: Optional[int] = 42) -> pygame.Surface:
        """Generates a surface containing the person's details.

        Args:
            font (pygame.freetype.Font)
            color (tuple, optional): Defaults to (0, 0, 0).
            font_size (int, optional): Defaults to 42.

        Returns:
            pygame.Surface: A surface containing the details
        """
        name, _ = font.render(f'{self.person.name}', fgcolor=color, size=font_size)
        birthday, _ = font.render(
            f'Born {self.person.ssid.birthday}', fgcolor=color, size=font_size)
        ssid, _ = font.render(f'{self.person.ssid}', fgcolor=color, size=font_size)
        height, _ = font.render(f'{self.person.height} cm', fgcolor=color, size=font_size)

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
