from random import choice
import sys
import os
import pygame
import pygame.freetype
from pygame.locals import QUIT
from logic.checkpoint import Checkpoint
from ui.person_sprite import PersonSprite

class Game:
    def __init__(self):
        self.fps = 60
        self.width = 1920   
        self.height = 1080

        pygame.init()
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Turukuun Pliis')

        self._init_fonts()
        self._init_images()

        self.checkpoint = Checkpoint()
        self.persons = pygame.sprite.Group()

        first_sprite = PersonSprite(self.checkpoint.current_person())
        first_sprite.set_image(self.random_sprite())
        first_sprite.rect.x = 420
        first_sprite.rect.y = 200
        self.persons.add(first_sprite)

    def _init_fonts(self) -> None:
        font_directory = os.path.join('data', 'fonts')
        self.font = pygame.freetype.Font(os.path.join(
            font_directory, 'VT323-Regular.ttf'), 42)

    def _init_images(self) -> None:
        image_directory = os.path.join('data', 'sprites')
        self.person_sprites = []

        # TODO: Dynamic loading?
        for filename in ('person.png', 'person2.png', 'person3.png'):
            sprite = pygame.image.load(
                os.path.join(image_directory, filename)
            )
            self.person_sprites.append(sprite)

    def tick(self) -> None:
        pygame.display.update()
        self.clock.tick(self.fps)

    def random_sprite(self) -> pygame.Surface:
        return choice(self.person_sprites)

    def menu(self) -> pygame.Surface:
        surface = pygame.Surface((self.width, self.height))
        surface.fill((150, 175, 250))

        logo, logo_rect = self.font.render('TURUKUUN PLIIS', size=72)
        logo_rect.center = (self.width / 2, self.height / 2 - 100)
        surface.blit(
            logo,
            logo_rect
        )

        start_instructions, start_instructions_rect = self.font.render(
            'PRESS SPACE TO START', size=42)
        start_instructions_rect.center = (self.width / 2, self.height / 2)

        quit_instructions, quit_instructions_rect = self.font.render(
            'PRESS ESC TO QUIT', size=42)
        quit_instructions_rect.center = (self.width / 2, self.height / 2 + 30)

        surface.blit(start_instructions, start_instructions_rect)
        surface.blit(quit_instructions, quit_instructions_rect)

        return surface

    def render_last(self, surface, sprite):
        self.font.render_to(surface, (100, 450), 'Last Person', (50, 50, 50))
        surface.blit(
            sprite.generate_details_surface(
                self.font, color=(125, 125, 125)),
            (100, 500)
        )

    def game(self) -> pygame.Surface:
        surface = pygame.Surface((self.width, self.height))

        surface.fill((150, 175, 250))
        self.font.render_to(
            surface,
            (10, 10),
            f'Checkpoint {self.checkpoint.name}',
            (0, 0, 0)
        )

        self.font.render_to(
            surface,
            (10, 60),
            'Objective:',
            (0, 0, 0)
        )
        self.font.render_to(
            surface,
            (10, 100),
            '- Check that details match',
            (0, 0, 0)
        )

        current = self.checkpoint.current_person()
        if current:
            surface.blit(
                self.persons.sprites()[0].generate_details_surface(self.font),
                (100, 200)
            )
        else:
            self.font.render_to(
                surface,
                (100, 200),
                'Queue is empty',
                (0, 0, 0)
            )
            self.render_last(surface, self.persons.sprites()[0])

        if len(self.persons.sprites()) > 1:
            self.render_last(surface, self.persons.sprites()[1])

        self.persons.draw(surface)
        return surface

    def next_person(self) -> None:
        next_person = self.checkpoint.next_person()

        last_sprite = self.persons.sprites()[0]
        self.persons.empty()

        if next_person:
            last_sprite.rect.y += 300

            next_sprite = PersonSprite(next_person)
            next_sprite.set_image(self.random_sprite())
            next_sprite.rect.x = 420
            next_sprite.rect.y = 200

            self.persons.add(next_sprite)
        else:
            last_sprite.rect.y = 200 + 300
        self.persons.add(last_sprite)

    def loop(self):
        in_menu = True

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if in_menu:
                        if event.key == pygame.K_SPACE:
                            in_menu = False

                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()

                    if not in_menu:
                        if event.key == pygame.K_ESCAPE:
                            in_menu = True

                        if event.key in (pygame.K_y, pygame.K_n):
                            self.next_person()

            if in_menu:
                self.window.blit(self.menu(), (0, 0))
            else:
                self.window.blit(self.game(), (0, 0))
            self.tick()
