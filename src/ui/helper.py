import pygame
from pygame.constants import SRCALPHA

from logic.game import Game


class Helper:
    """Common methods."""
    @staticmethod
    def centered_text(
        surface: pygame.Surface,
        font: pygame.freetype.Font,
        text: str,
        size: int = 42,
        offsets: tuple = (0, 0)
    ) -> None:
        """Blits centered text on pygame surface.

        Args:
            surface (pygame.Surface): the surface to blit onto.
            font (pygame.freetype.Font): the font to render with.
            text (str): the text to render.
            size (int, optional): font size.
                Defaults to 42.
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

    @staticmethod
    def combined_surface(
        surfaces: list[pygame.Surface],
        padding: int = 10
    ) -> pygame.Surface:
        """Returns a combined surface from the surfaces given.
        Will stack the surfaces on a vertical stack in list order.

        Args:
            surfaces (list[pygame.Surface]): list of surfaces.
            padding (int, optional): padding between surfaces. Defaults to 10.

        Returns:
            pygame.Surface: the combined surface.
        """
        width = max(map(lambda surf: surf.get_width(), surfaces))
        height = sum(map(lambda surf: surf.get_height(), surfaces)) + \
            len(surfaces) * padding

        surface = pygame.Surface(
            (
                width,
                height
            ),
            SRCALPHA
        )

        current_height = 0
        for surf in surfaces:
            surface.blit(
                surf,
                (
                    0,
                    current_height
                )
            )

            current_height += surf.get_height()
            current_height += padding

        return surface

    @staticmethod
    def multiline_text(
        font: pygame.freetype.Font,
        multiline_text: str,
        size: int = 42,
        color: tuple = (0, 0, 0),
        padding: int = 10
    ) -> pygame.Surface:
        """Naive multiline text surface generator.
        No checks for max width or height.

        Args:
            font (pygame.freetype.Font): the font to render with.
            text (str): the text to render.
            size (int, optional): font size. Defaults to 42.
            padding (int, optional): padding between lines. Defaults to 10.

        Returns:
            pygame.Surface: a surface with the multiline text.
        """

        lines = [
            font.render(text, size = size, fgcolor = color)[0]
            for text in multiline_text.split('\n')
        ]
        return Helper.combined_surface(lines, padding)


    @staticmethod
    def point_explanation(game: Game) -> str:
        text = 'CURRENT SCORING:\n'
        text += f'{game.points_for_correct_approval} points for correct approvals.\n'
        text += f'{game.points_for_incorrect_approval} points for incorrect approvals.\n'
        text += f'{game.points_for_correct_rejection} points for correct rejections.\n'
        text += f'{game.points_for_incorrect_rejection} points for incorrect rejections.'
        return text
