from random import choice
from random import randint
from random import randrange
from random import shuffle
from data.utility import get_pds, wrong_localizations, GenerateException


class Generator:
    """A class, that generates fictional data"""

    def __init__(self, data="data", folder="data"):
        """Initialize the class object and collect all the data together
        pds - personal data
        available_locales - locales, that are available now"""
        self.pds = get_pds(data, folder)
        self.wrong_localizations = wrong_localizations
        self.available_locales = list(self.pds.keys())

    def random_person(self, parameter, loc):
        """Depending on parameter randomize different persons"""
        self.check_attributes(["first_names_male", "last_names_male", "first_names_female", "last_names_female"],
                              loc, 'person')
        if parameter == "m":
            return f"{choice(self.pds[loc].person.first_names_male)} " \
                   f"{choice(self.pds[loc].person.last_names_male)}"
        if parameter == "f":
            return f"{choice(self.pds[loc].person.first_names_female)} " \
                   f"{choice(self.pds[loc].person.last_names_female)}"

    def random_address(self, loc):
        self.check_attributes(['city_names', 'street_titles'], loc, 'address')
        """Randomize address from address_data"""
        return f"{choice(self.pds[loc].address.city_names)} " \
               f"{choice(self.pds[loc].address.street_titles)} {randint(1, 200)}"

    def random_job(self, loc):
        """Randomize job from job_data"""
        self.check_attributes(['jobs'], loc, 'job')
        return f"{choice(self.pds[loc].job.jobs)}"

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

    def check_attributes(self, attributes, loc, file):
        attributes = attributes
        not_founded = []
        for a in attributes:
            if not hasattr(getattr(self.pds[loc], file), a):
                not_founded.append(a)

        if not_founded:
            raise GenerateException(f"Not founded following attributes: {not_founded} in 'person.py' file "
                                    f"for '{loc}' localization. Please check it!")
