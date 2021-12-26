import json
import requests

from requests.exceptions import RequestException

class Sheets:
    def __init__(self, base_url: str = None):
        # Not as a parameter default value because it looks ugly
        if not base_url:
            base_url = 'https://sheetdb.io/api/v1/l92ty9ctz6565'
        self.base_url = base_url
    def get_column_as_list(self, sheet: str, column: str) -> list[str]:
        url = f'{self.base_url}/?sheet={sheet}'
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
