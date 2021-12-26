import os.path

class Local:
    """Class for handling local storage (files).

    Attributes:
        folder (str): the folder to store data in."""
    def __init__(self, folder: str = 'data') -> None:
        """Initializes Local.

        Args:
            folder (str, optional): the folder for storing data.
                Defaults to 'data'.
        """
        self.folder = folder

    def get_path(self, filename: str) -> os.path:
        """Returns the correct path to the file.

        Args:
            filename (str)

        Returns:
            os.path: path to the file.
        """
        return os.path.join(self.folder, filename)

    def save_string_list(self, string_list: list[str], filename: str) -> bool:
        """Saves a list of strings into a file.
        Saves as comma-seperated values (csv)
        See read_string_list

        Args:
            string_list (list[str]): the list of strings to save.
            filename (str)

        Returns:
            bool: if the save was successful.
        """
        if any(',' in string for string in string_list):
            return False

        try:
            with open(self.get_path(filename), 'w', encoding = 'utf-8') as file:
                file.write(','.join(string_list))
            return True
        except IOError as error:
            print(f'{error}')
            return False

    def read_string_list(self, filename: str) -> list[str]:
        """Reads a list of strings from a file.
        Assumes the format is comma-seperated values (csv)
        See save_string_list

        Args:
            filename (str)

        Returns:
            list[str]: the list containing values read from the file.
        """
        path = self.get_path(filename)
        if not os.path.exists(path):
            return None

        try:
            with open(path, 'r', encoding = 'utf-8') as file:
                return file.read().split(',')
        except IOError as error:
            print(f'{error}')
            return None
