from random import randrange, choice
from typing import Optional

from logic.ssid import SSID

BASE_YEAR = 2020

# TODO: Pull data from e.g. dvv statistics excel sheet
def random_name():
    first = choice(
        # n > 10 000 with last 3 added for padding, for both dvv-listed groupings
        [
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
            "Lasse", "Kullervo", "Jyrki", "Keijo",

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
            "Maritta", "Outi", "Milla", "Emmi",
        ]
    )

    # top 100 last names
    last = choice(
        [
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
            "Karppinen", "Rissanen", "Mäki", "Laukkanen",
        ]
    )

    return f'{first} {last}'

class Person():
    """A class representing an in-game person

    Attributes:
        name (str): the name of this person.
        age (int): the age of this person in years.
        height (int): the height of this person in cm.
        ssid (SSID): the SSID of this person.
    """
    def __init__(self,
                 name: Optional[str] = None,
                 age: Optional[int] = None,
                 height: Optional[int] = None,
                 ssid: Optional[SSID] = None) -> None:
        """Initializes Person.

        Args:
            name (str, optional): The name of the person.
                Defaults to a random Finnish name.
            age (int, optional): The age of the person.
                Defaults to a value between [12, 80[.
            height (int, optional): The height of the person.
                Defaults to a value between [150, 220[.
            ssid (SSID, optional): The SSID of the person.
                Defaults to a randomly generated SSID based on age.
        """
        if not name:
            name = random_name()
        if not age:
            age = randrange(12, 80)
        if not height:
            height = randrange(150, 220)
        if not ssid:
            ssid = SSID.random(age)

        self.name = name
        self.age = age
        self.height = height
        self.ssid = ssid

    def __repr__(self) -> str:
        return f'{self.name} {self.ssid}'
