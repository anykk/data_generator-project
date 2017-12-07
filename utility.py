from os import listdir, sep
from os.path import abspath
import json


def get_jsons(folder="data"):
    """Identify all json files from any path."""
    jsons = []
    for data in listdir(folder):
        if data.endswith(".json"):
            jsons.append(data)
    return jsons


def parse(filename):
    """Parse json dicts from file. If can't parse => empty dict."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except json.decoder.JSONDecodeError:
        return dict()


def get_pds(folder="data"):
    """Get personal all data dicts (wrong too)"""
    jsons = get_jsons(folder)
    localizations_names = map(lambda x: x[0: -5], jsons)
    localizations_data = map(lambda x: parse(folder + sep + x), jsons)
    return folder, dict(zip(localizations_names, localizations_data))


class LocalizationNotFoundError(Exception):
    """Throws when localization was not found in data folder."""
    def __init__(self, name, folder):
        super().__init__()
        self.name = name
        self.folder = folder

    def __str__(self):
        return f"LocalizationNotFoundError: Not found '{self.name}.json' localization file for " \
               f"'{self.name}' localization in '{abspath(self.folder)}' folder!"


class NotFullLocalizationError(Exception):
    """Throws when localization was found in data folder, but some dict keys was not found."""
    def __init__(self, name, folder, keys):
        super().__init__()
        self.name = name
        self.folder = folder
        self.keys = keys

    def __str__(self):
        return f"GenerateError: In '{abspath(self.name + '.json')}' localization file for '{self.name}' " \
               f"localization missed following keys: {self.keys}"


class NothingGeneratedError(Exception):
    """Throws when all dict keys are present but some is empty."""
    def __init__(self, name, folder, keys):
        super().__init__()
        self.name = name
        self.folder = folder
        self.keys = keys

    def __str__(self):
        return f"NothingGeneratedError: In {abspath(self.name) + '.json'} localization file for '{self.name}' " \
               f"localization {self.keys} is empty or 'broken'."


class InvalidArgumentError(Exception):
    """Throws when any argument is invalid"""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"InvalidArgumentError: {self.message}."