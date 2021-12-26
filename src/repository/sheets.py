import json
import requests

from requests.exceptions import RequestException

BASE_URL = 'https://sheetdb.io/api/v1/l92ty9ctz6565'

class Sheets:
    def get_column_as_list(self, sheet: str, column: str) -> list[str]:
        url = f'{BASE_URL}/?sheet={sheet}'
        try:
            response = json.loads(
                requests.get(url).content
            )
            return [row[column] for row in response]
        except RequestException as error:
            print(f'{error}')
            return None

    def get_male_first_names(self) -> list[str]:
        return self.get_column_as_list('male_first_names', 'name')

    def get_female_first_names(self) -> list[str]:
        return self.get_column_as_list('female_first_names', 'name')

    def get_surnames(self) -> list[str]:
        return self.get_column_as_list('surnames', 'surname')
