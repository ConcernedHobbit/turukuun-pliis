from datetime import date
from random import randrange
from typing import Optional

class SSID:
    def __init__(self, birthday: date, individual_number: Optional[int]=None) -> None:
        if 1800 <= birthday.year < 2100:
            self.birthday = birthday
        else:
            raise ValueError('SSID is not defined for years before 1800 or after 2099')

        print(individual_number)

        if individual_number is None:
            self.individual_number = randrange(2, 900)
        else:
            if 2 <= individual_number < 900:
                self.individual_number = individual_number
            else:
                raise ValueError('SSID individual number should be between 2 and 899 (inclusive)')

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

    def __repr__(self) -> str:
        return f'{self._date}{self._seperator}{self._padded_individual_number}{self._checkdigit}'

class Person:
    def __init__(self, name: str, age: int, height: int) -> None:
        self.name = name
        self.age = age
        self.height = height
