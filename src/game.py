from datetime import date
from random import randrange
import sys
import os
import pygame
import pygame.freetype
from pygame.locals import QUIT
from person import Person

# constants
FPS = 60
WIDTH = 800
HEIGHT = 800

# initialization
pygame.init()
clock = pygame.time.Clock()
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Turukuun Pliis')

# font
FONT_DIRECTORY = os.path.join('data', 'fonts')
FONT = pygame.freetype.Font(os.path.join(FONT_DIRECTORY, 'VT323-Regular.ttf'), 42)

# images
IMAGE_DIRECTORY = os.path.join('data', 'sprites')
PERSON_SPRITE = pygame.image.load(os.path.join(IMAGE_DIRECTORY, 'person.png'))
PERSON2_SPRITE = pygame.image.load(os.path.join(IMAGE_DIRECTORY, 'person2.png'))
PERSON3_SPRITE = pygame.image.load(os.path.join(IMAGE_DIRECTORY, 'person3.png'))
def random_sprite() -> pygame.Surface:
    return [PERSON_SPRITE, PERSON2_SPRITE, PERSON3_SPRITE][randrange(3)]

# sprites
visitors = pygame.sprite.Group()

person = Person()
person.set_image(PERSON_SPRITE)
person.rect.x = 420
person.rect.y = 200

visitors.add(person)

day = date(2020, 3, 26)

def start():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y or event.key == pygame.K_n:
                    last_person = visitors.sprites()[0]
                    last_person.rect.y += 300
                    visitors.empty()

                    new_person = Person()
                    new_person.set_image(random_sprite())
                    new_person.rect.x = 420
                    new_person.rect.y = 200

                    visitors.add(new_person)
                    visitors.add(last_person)

        WINDOW.fill((150, 175, 250))
        FONT.render_to(WINDOW, (10, 10), 'Turukuun Pliis', (0, 0, 0))

        day_text, day_text_rect = FONT.render(f'{day}', (0, 0, 0))
        day_text_rect.topright = (WINDOW.get_width() - 10, 10)
        WINDOW.blit(day_text, day_text_rect)

        FONT.render_to(WINDOW, (10, 60), 'Objective:', (0, 0, 0))
        FONT.render_to(WINDOW, (10, 100), '- Check that details match', (0, 0, 0))

        WINDOW.blit(
            visitors.sprites()[0].generate_details_surface(FONT),
            (100, 200)
        )

        if len(visitors.sprites()) > 1:
            FONT.render_to(WINDOW, (100, 450), 'Last Person', (50, 50, 50))
            WINDOW.blit(
                visitors.sprites()[1].generate_details_surface(FONT, color = (125, 125, 125)),
                (100, 500)
            )

        FONT.render_to(WINDOW,
            (10, WINDOW.get_height() - FONT.size - 10),
            'Press n to turn away, y to let through',
            (175, 0, 0)
        )

        visitors.update()
        visitors.draw(WINDOW)

        pygame.display.update()
        clock.tick(FPS)
