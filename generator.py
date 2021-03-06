from random import choice, randint, randrange, shuffle
from utility import NotFullLocalizationError, NothingGeneratedError, InvalidArgumentError


class Generator:
    """A class, that generates fictional data"""
    def __init__(self, data):
        """Initialize the class object and collect all data together
        pds - personal data
        available_locales - locales, that are available now"""
        self._data_folder, self._pds = data
        self._available_locales = list(self._pds.keys())

    @property
    def pds(self):
        return self._pds

    @property
    def available_locales(self):
        return self._available_locales

    @property
    def data_folder(self):
        return self._data_folder

    def random_person(self, parameter, loc):
        """Depending on parameter randomize different persons"""
        if parameter != "m" and parameter != "f":
                raise InvalidArgumentError(f"argument '{parameter}' doesn't support. Please use 'm' or 'f' for it.")
        self._check_keys(loc, self._data_folder)
        try:
            return f"{choice(self._pds[loc]['person'][parameter]['first_name'])} " \
                   f"{choice(self._pds[loc]['person'][parameter]['last_name'])}"
        except IndexError:
            raise NothingGeneratedError(loc, self._data_folder,
                                        '{"0": {"person": {"1": {"first_name/last_name": }}}}'
                                        .replace("0", loc).replace("1", parameter))

    def random_address(self, loc):
        """Randomize address from address_data"""
        self._check_keys(loc, self._data_folder)
        try:
            return f"{choice(self._pds[loc]['address']['city'])} " \
                   f"{choice(self._pds[loc]['address']['street'])} {randint(1, 200)}"
        except IndexError:
            raise NothingGeneratedError(loc, self._data_folder,
                                        '{"0": {"address": {"city/street": }}}'.replace("0", loc))

    def random_job(self, loc):
        """Randomize job from job_data"""
        self._check_keys(loc, self._data_folder)
        try:
            return f"{choice(self._pds[loc]['job'])}"
        except IndexError:
            raise NothingGeneratedError(loc, self._data_folder,
                                        '{"0": {"job": }}'.replace("0", loc))

    @staticmethod
    def average_age(n):
        """Generates a 'average' age if n is not a zero"""
        if n == 0:
            return randint(1, 100)
        elif 6 > n > 3:
            return randint(n - 3, n + 3)
        else:
            return randint(n - 5, n + 5)

    @staticmethod
    def phone_number():
        """Generates a random phone number, but not 'smart'
        it will be reworked later, maybe"""
        return 89000000000 + randint(0, 999999999)

    @staticmethod
    def password(n):
        """Generates a random password. Recommend length >= 8."""
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        upper_alphabet = alphabet.upper()
        pw_list = []

        for i in range(n // 3):
            pw_list.append(alphabet[randrange(len(alphabet))])
            pw_list.append(upper_alphabet[randrange(len(upper_alphabet))])
            pw_list.append(str(randrange(10)))
        for i in range(n - len(pw_list)):
            pw_list.append(alphabet[randrange(len(alphabet))])

        shuffle(pw_list)
        return "".join(pw_list)

    def _check_keys(self, loc, file):
        """Check that keys are exist in pds dictionary and claim all not existing."""
        not_founded = {}
        if "address" not in self._pds[loc]:
            not_founded.update({"address": {"city": "(...)", "street": "(...)"}})
        else:
            if "city" not in self._pds[loc]["address"]:
                not_founded.update({"address": {"city": "(...)"}})
            if "street" not in self._pds[loc]["address"]:
                not_founded.update({"address": {"street": "(...)"}})
        if "job" not in self._pds[loc]:
            not_founded.update({"job": "(...)"})
        if "person" not in self._pds[loc]:
            not_founded.update({"person": {"m": {"first_name": "(...)", "last_name": "(...)"},
                                           "f": {"first_name": "(...)", "last_name": "(...)"}}})
        else:
            if "m" not in self._pds[loc]["person"]:
                not_founded.update({"person": {"m": {"first_name": "(...)", "last_name": "(...)"}}})
            else:
                if "first_name" not in self._pds[loc]["person"]["m"]:
                    not_founded.update({"person": {"m": {"first_name": "(...)"}}})
                if "last_name" not in self._pds[loc]["person"]["m"]:
                    not_founded.update({"person": {"m": {"last_name": "(...)"}}})
            if "f" not in self._pds[loc]["person"]:
                not_founded.update({"person": {"first_name": "(...)", "last_name": "(...)"}})
            else:
                if "first_name" not in self._pds[loc]["person"]["f"]:
                    not_founded.update({"person": {"f": {"first_name": "(...)"}}})
                if "last_name" not in self._pds[loc]["person"]["f"]:
                    not_founded.update({"person": {"f": {"last_name": "(...)"}}})
        if not_founded:
            raise NotFullLocalizationError(loc, file, not_founded)
