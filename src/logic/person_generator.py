from service.name_service import NameService
from logic.person import Person

class PersonGenerator:
    def __init__(self, name_service: NameService):
        self.name_service = name_service

    def get_person(self) -> Person:
        return Person(
            self.name_service.random_name()
        )
