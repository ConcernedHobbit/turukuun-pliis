from __future__ import annotations
from datetime import date
from random import random, randrange
from logic.entry_documents.entry_document import EntryDocument
from logic.person import Person, PersonDetails
from logic.ssid import SSID

class Passport(EntryDocument):
    """An EntryDocument representing the basic details of a Person.

    Attributes:
        name (str):, will always be 'Passport'.
        person (Person): who this passport belongs to.
        details (PersonDetails): the details on this passport.
        valid (bool): if the details match for the person and passport.
        reason_not_valid (str): the reason(s) this passport is not valid,
            one reason on each line.
    """
    def __init__(self,
                 person: Person,
                 details_on_passport: PersonDetails = None) -> None:
        """Initializes Passport.

        Args:
            person (Person): who this passport belongs to.
            details_on_passport (PersonDetails, optional): the details on this passport.
                Defaults to the person's details.
        """
        super().__init__('Passport')

        self.person = person

        if not details_on_passport:
            details_on_passport = self.person.details
        self.details = details_on_passport

        if not self.person.details == self.details:
            self.valid = False

            differences = PersonDetails.differences(
                self.person.details,
                self.details
            )

            for difference in differences:
                reason = f'{difference.capitalize()} does not match'

                if not self.reason_not_valid:
                    self.reason_not_valid = reason
                else:
                    self.reason_not_valid += f'\n{reason}'

    @staticmethod
    def generate_fake(person: Person, difficulty: int = 0) -> Passport:
        """Generates a fake Passport.

        Args:
            person (Person): the person this fake passport belongs to.
            difficulty (int, optional): difficulty, with 0 being easiest to spot.
                Defaults to 0.

        Returns:
            Passport: a passport with random wrong details based on difficulty.
        """
        details = person.details
        if difficulty == 0:
            if random() < 0.5:
                # Mutate name
                first, last = person.name.split()
                if random() < 0.75:
                    # Mutate last name completely
                    # TODO: Make this not dirty, e.g. seperate random_last_name method somewhere
                    new_last = last
                    while new_last == last:
                        new_last = Person().name.split()[1]
                    last = new_last
                else:
                    # Mutate first name completely
                    # TODO: Make this not dirty, e.g. seperate random_first_name method somewhere
                    new_first = first
                    while new_first == first:
                        new_first = Person().name.split()[0]
                    first = new_first
                details.name = f'{first} {last}'
            else:
                # Mutate age
                difference = randrange(-2, 2)
                details.age = person.age + difference
                details.ssid = SSID(
                    date(
                        person.ssid.birthday.year + difference,
                        person.ssid.birthday.month,
                        person.ssid.birthday.day
                    ),
                    person.ssid.individual_number
                )
        else:
            NotImplementedError()

        return Passport(person, details)
