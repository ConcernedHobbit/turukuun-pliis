from random import choice
from typing import Callable
from repository.local import Local
from repository.sheets import Sheets

BACKUP_MALE_LIST = [
    "Juhani", "Olavi", "Antero", "Tapani",
    "Johannes", "Tapio", "Mikael", "Kalevi",
    "Matti", "Pekka", "Petteri", "Ilmari",
    "Sakari", "Matias", "Antti", "Juha",
    "Kristian", "Heikki", "Timo", "Mikko",
    "Kari", "Markus", "Aleksi", "Jari",
    "Jukka", "Markku", "Oskari", "Jaakko",
    "Kalervo", "Petri", "Mika", "Henrik",
    "Lauri", "Veikko", "Hannu", "Ville",
    "Erkki", "Seppo", "Valtteri", "Janne",
    "Ari", "Marko", "Ensio", "Tuomas",
    "Sami", "Elias", "Juho", "Pentti",
    "Eero", "Erik", "Martti", "Jani",
    "Onni", "Eemeli", "Samuli", "Jorma",
    "Jussi", "Harri", "Teemu", "Eino",
    "Risto", "Samuel", "Jarmo", "Veli",
    "Esa", "Raimo", "Pasi", "Pertti",
    "Jouni", "Viljami", "Niko", "Arto",
    "Olli", "Joonas", "Esko", "Emil",
    "Vesa", "Kalle", "Oliver", "Toivo",
    "Toni", "Jouko", "Leo", "Reijo",
    "Paavo", "Armas", "Santeri", "Johan",
    "Tomi", "Kimmo", "Väinö", "Henri",
    "Eetu", "Joni", "Daniel", "Tommi",
    "Tero", "Alexander", "Sebastian", "Ilkka",
    "Otto", "Pauli", "Ilari", "Eemil",
    "Anton", "Aleksanteri", "Uolevi", "Jarkko",
    "Tuomo", "Jalmari", "Jesse", "Joona",
    "Akseli", "Aulis", "Benjamin", "Vilho",
    "Julius", "Arttu", "Joel", "Jere",
    "Juuso", "Simo", "Leevi", "Christian",
    "Allan", "Niilo", "Einari", "Niklas",
    "Lasse", "Kullervo", "Jyrki", "Keijo"
]

BACKUP_FEMALE_LIST = [
    "Maria", "Helena", "Anneli", "Johanna",
    "Kaarina", "Hannele", "Marjatta", "Kristiina",
    "Emilia", "Liisa", "Elina", "Sofia",
    "Tuulikki", "Maarit", "Susanna", "Annikki",
    "Katariina", "Leena", "Anna", "Marja",
    "Sinikka", "Inkeri", "Riitta", "Aino",
    "Anne", "Tuula", "Kyllikki", "Päivi",
    "Orvokki", "Ritva", "Maija", "Karoliina",
    "Tellervo", "Pauliina", "Minna", "Pirjo",
    "Sari", "Irmeli", "Eveliina", "Tiina",
    "Eeva", "Laura", "Marika", "Elisabet",
    "Tarja", "Satu", "Mari", "Pirkko",
    "Hanna", "Heidi", "Annika", "Marita",
    "Ilona", "Seija", "Sirpa", "Jaana",
    "Amanda", "Anja", "Sanna", "Irene",
    "Raija", "Julia", "Sisko", "Anita",
    "Kirsi", "Eija", "Marianne", "Eila",
    "Matilda", "Aurora", "Olivia", "Katriina",
    "Merja", "Elisabeth", "Anni", "Tuulia",
    "Arja", "Linnea", "Marjaana", "Ulla",
    "Kaisa", "Marketta", "Paula", "Elisa",
    "Helmi", "Jenni", "Terttu", "Sirkka",
    "Iida", "Emma", "Katja", "Heli",
    "Mirjami", "Nina", "Maaria", "Anniina",
    "Kirsti", "Mirja", "Sara", "Hilkka",
    "Birgitta", "Ella", "Raili", "Katri",
    "Ida", "Aleksandra", "Suvi", "Alexandra",
    "Riikka", "Kaija", "Marjut", "Anu",
    "Tuija", "Saara", "Niina", "Pia",
    "Kerttu", "Lea", "Kristina", "Noora",
    "Aila", "Marjo", "Jenna", "Tanja",
    "Ellen", "Leila", "Veera", "Lotta",
    "Irma", "Henna", "Marja-Leena", "Kati",
    "Aulikki", "Alina", "Margareta", "Elsa",
    "Elli", "Irja", "Hellevi", "Marja-Liisa",
    "Maritta", "Outi", "Milla", "Emmi"
]

BACKUP_SURNAME_LIST = [
    "Korhonen", "Virtanen", "Mäkinen", "Nieminen",
    "Mäkelä", "Hämäläinen", "Laine", "Heikkinen",
    "Koskinen", "Järvinen", "Lehtonen", "Lehtinen",
    "Saarinen", "Salminen", "Heinonen", "Niemi",
    "Heikkilä", "Kinnunen", "Salonen", "Turunen",
    "Salo", "Laitinen", "Tuominen", "Rantanen",
    "Karjalainen", "Jokinen", "Mattila", "Savolainen",
    "Lahtinen", "Ahonen", "Ojala", "Leppänen",
    "Kallio", "Leinonen", "Väisänen", "Hiltunen",
    "Miettinen", "Pitkänen", "Aaltonen", "Manninen",
    "Koivisto", "Hakala", "Anttila", "Laaksonen",
    "Hirvonen", "Lehto", "Räsänen", "Laakso",
    "Toivonen", "Rantala", "Mustonen", "Aalto",
    "Niemelä", "Nurmi", "Peltonen", "Moilanen",
    "Seppälä", "Pulkkinen", "Hänninen", "Saari",
    "Kettunen", "Lappalainen", "Partanen", "Kemppainen",
    "Kauppinen", "Koskela", "Seppänen", "Ahola",
    "Lahti", "Salmi", "Huttunen", "Ikonen",
    "Aho", "Suominen", "Kärkkäinen", "Pesonen",
    "Halonen", "Nyman", "Koponen", "Mikkonen",
    "Peltola", "Johansson", "Oksanen", "Lindholm",
    "Niskanen", "Vainio", "Heiskanen", "Mikkola",
    "Koski", "Honkanen", "Immonen", "Nurminen",
    "Vuorinen", "Harju", "Määttä", "Kokkonen",
    "Karppinen", "Rissanen", "Mäki", "Laukkanen"
]

FEMALE_FIRST_NAMES = 'names_female.csv'
MALE_FIRST_NAMES = 'names_male.csv'
SURNAMES = 'surname.csv'

class NameService:
    def __init__(self, local_repo: Local, sheets_repo: Sheets):
        self.local_repo = local_repo
        self.sheets_repo = sheets_repo

        self.female_list = self._load(
            FEMALE_FIRST_NAMES,
            self.sheets_repo.get_female_first_names,
            BACKUP_FEMALE_LIST
        )

        self.male_list = self._load(
            MALE_FIRST_NAMES,
            self.sheets_repo.get_male_first_names,
            BACKUP_MALE_LIST
        )

        self.surname_list = self._load(
            SURNAMES,
            self.sheets_repo.get_surnames,
            BACKUP_SURNAME_LIST
        )

    def _load(self,
              filename: str,
              internet_getter: Callable,
              backup_list: list) -> list[str]:
        """Load name list.
        Tries to load from local file first.
        If no local file is found, attempts to get list from internet.
        If the list was successfully retrieved from the internet, saves it locally.
        Loads a backup list if all else fails.

        Args:
            filename (str): local copy's filename.
            internet_getter (Callable): method to get the list from the internet.
            backup_list (list)

        Returns:
            list[str]: the list of names.
        """
        names = self.local_repo.read_string_list(filename)
        if not names:
            names = internet_getter()
            if names:
                self.local_repo.save_string_list(
                    names,
                    filename
                )
            else:
                names = backup_list
        return names

    def random_female_first_name(self) -> str:
        return choice(self.female_list)

    def random_male_first_name(self) -> str:
        return choice(self.male_list)

    def random_first_name(self) -> str:
        return choice([
            self.random_female_first_name(),
            self.random_male_first_name()
        ])

    def random_surname(self) -> str:
        return choice(self.surname_list)

    def random_female_name(self) -> str:
        return f'{self.random_female_first_name()} {self.random_surname()}'

    def random_male_name(self) -> str:
        return f'{self.random_male_first_name()} {self.random_surname()}'

    def random_name(self) -> str:
        return choice([self.random_male_name(), self.random_female_name()])
