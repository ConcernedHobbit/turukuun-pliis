from __future__ import annotations
from dataclasses import dataclass
from random import randrange
from typing import Optional

from logic.entry_documents.entry_document import EntryDocument
from logic.ssid import SSID

BASE_YEAR = 2020
@dataclass
class PersonDetails():
    """Class representing a person's details"""
    name: str
    age: int
    height: int
    ssid: SSID

    @staticmethod
    def differences(details: PersonDetails, other_details: PersonDetails) -> list:
        diff = []
        for key, details_value, other_details_value in zip(
            vars(details).keys(),
            vars(details).values(),
            vars(other_details).values()):
            if details_value != other_details_value:
                diff.append(key)
        return diff

class Person():
    """Class representing an in-game person

    Attributes:
        name (str): the name of this person.
        age (int): the age of this person in years.
        height (int): the height of this person in cm.
        ssid (SSID): the SSID of this person.
        entry_documents (list[EntryDocument]): the entry documents of this person.
    """
    def __init__(self,
                 name: Optional[str] = 'Matti Meikäläinen',
                 age: Optional[int] = None,
                 height: Optional[int] = None,
                 ssid: Optional[SSID] = None,
                 entry_documents: Optional[list[EntryDocument]] = None) -> None:
        """Initializes Person.

        Args:
            name (str, optional): The name of the person.
                Defaults to 'Matti Meikäläinen'.
            age (int, optional): The age of the person.
                Defaults to a value between [12, 80[.
            height (int, optional): The height of the person.
                Defaults to a value between [150, 220[.
            ssid (SSID, optional): The SSID of the person.
                Defaults to a randomly generated SSID based on age.
            entry_documents (list[EntryDocument], optional): The entry documents of the person.
                Defaults to an empty list.
        """
        if not age:
            age = randrange(12, 80)
        if not height:
            height = randrange(150, 220)
        if not ssid:
            ssid = SSID.random(age)
        if not entry_documents:
            entry_documents = []

        self.name = name
        self.age = age
        self.height = height
        self.ssid = ssid
        self.entry_documents = entry_documents

    @property
    def details(self) -> PersonDetails:
        """
        Returns:
            PersonDetails: this person's details wrapped in a PersonDetails instance
        """
        return PersonDetails(
            self.name,
            self.age,
            self.height,
            self.ssid
        )

    def get_entry_document(self, name: str) -> Optional[EntryDocument]:
        """Get an entry document by name

        Args:
            name (str): name of the entry document.

        Returns:
            Optional[EntryDocument]: the entry document or None if not found.
        """
        return next(
            (document for document in self.entry_documents if document.name == name),
            None
        )

    def has_entry_document(self, name: str) -> bool:
        """Check whether or not an entry document with name exists.

        Args:
            name (str): name of the entry document.

        Returns:
            bool: if the person has such an entry document.
        """
        return any(document.name == name for document in self.entry_documents)

    def __repr__(self) -> str:
        return f'{self.name} {self.ssid}'
