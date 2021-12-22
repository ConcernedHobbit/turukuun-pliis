from datetime import date
from random import randrange
from typing import Optional

from logic.ssid import SSID

BASE_YEAR = 2020


# TODO: Seperate sprite logic into an encapsulating class to abstract it away from game logic
class Person():
    """
    A class representing an in-game person
    """
    def __init__(self,
                 name: Optional[str] = 'Matti Meikäläinen', # TODO: Random generation
                 age: Optional[int] = randrange(12, 80),
                 height: Optional[int] = randrange(150, 220),
                 ssid: Optional[SSID] = None) -> None:
        """
        The constructor for class Person.

        Args:
            name (str, optional): The name of the person.
                Defaults to 'Matti Meikäläinen'.
            age (int, optional): The age of the person.
                Defaults to a value between [12, 80[.
            height (int, optional): The height of the person.
                Defaults to a value between [150, 220[.
            ssid (SSID, optional): The SSID of the person.
                Randomly generates one based on age if not provided.
        """

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

    def __repr__(self) -> str:
        return f'{self.name} {self.ssid}'
