from datetime import date
from random import randrange
from typing import Optional

class SSID:
    """
    A class representing a Finnish personal identity code (henkilötunnus)

    More information: https://dvv.fi/en/personal-identity-code
    """
    def __init__(self,
                 birthday: date,
                 individual_number: Optional[int] = randrange(2, 900)) -> None:
        """
        Constructor for SSID

        Args:
            birthday (date): The birthday this SSID will correspond to
            individual_number (int, optional): The individual number of this SSID.
                Defaults to randrange(2, 900).

        Raises:
            ValueError: If birthday is outside the range of [1800, 2099]
            ValueError: If the individual number is outside the range of [2, 899]
        """
        if 1800 <= birthday.year < 2100:
            self.birthday = birthday
        else:
            raise ValueError('SSID is not defined for years before 1800 or after 2099')

        if 2 <= individual_number < 900:
            self.individual_number = individual_number
        else:
            raise ValueError(
                'SSID individual number should be between 2 and 899 (inclusive)')

    @property
    def _date(self) -> str:
        """
        Returns:
            str: Birthday in format ddmmyy
        """
        # date.strftime cannot process years before 1900, so we need to manually format...
        return f'{self.birthday.day:02d}{self.birthday.month:02d}{str(self.birthday.year)[2:]}'

    @property
    def _padded_individual_number(self) -> str:
        """
        Returns:
            str: The individual number left-padded with zeroes
        """
        return str(self.individual_number).zfill(3)

    @property
    def _niner(self) -> str:
        """
        Returns:
            str: The birthday in format ddmmyy followed by the zero-padded individual number
        """
        return f'{self._date}{self._padded_individual_number}'

    @property
    def _checkdigit(self) -> str:
        """
        Returns the checkdigit of this SSID.
        Based on a mod 31 operation on the niner property.
        More information: https://dvv.fi/en/personal-identity-code
        Returns:
            str: The checkdigit for this SSID
        """
        mod = int(self._niner) % 31
        return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
                'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'][mod]

    @property
    def _seperator(self) -> str:
        """
        Returns:
            str: The century-defined seperator for this SSID
        """
        century = self.birthday.year // 100

        if century == 18:
            return '+'

        if century == 19:
            return '-'

        # since constructor does not accept invalid years, we can assume that we are in the 20xx
        # will have to be updated once dvv specifices symbol for 21xx
        return 'A'

    def matches_birthyear(self, year: int) -> bool:
        """
        Checks if this SSID matches a given birthyear

        Args:
            year (int): The year to check against

        Returns:
            bool: If this SSID matches the birthyear
        """
        return self.birthday.year == year

    @staticmethod
    def random(age: int):
        year = 2020 - age
        month = randrange(8, 13)
        day = randrange(1, 30)
        birthday = date(year, month, day)

        return SSID(birthday)


    def __repr__(self) -> str:
        return f'{self._date}{self._seperator}{self._padded_individual_number}{self._checkdigit}'
