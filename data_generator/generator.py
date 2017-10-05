import sys
import argparse
from random import choice as choice
from random import randint as randint
from random import randrange as randrange
from random import shuffle as shuffle

import data.address.ru as address_data_ru
import data.address.en as address_data_en

import data.job.ru as job_data_ru
import data.job.en as job_data_en

import data.person.ru as person_data_ru
import data.person.en as person_data_en


class Generator(object):
    """A class, that generates fictional data"""

    def __init__(self):
        """Initialize the class object and collect all the data together"""
        self.pd_ru = person_data_ru
        self.pd_en = person_data_en
        self.ad_ru = address_data_ru
        self.ad_en = address_data_en
        self.jd_ru = job_data_ru
        self.jd_en = job_data_en

    def random_person(self, parameter, loc):
        """Depending on parameter randomize different persons"""
        if loc == 'ru':
            if parameter == "m":
                return f"{choice(self.pd_ru.last_names_male)} " \
                       f"{choice(self.pd_ru.first_names_male)} " \
                       f"{choice(self.pd_ru.middle_names_male)}"
            if parameter == "f":
                return f"{choice(self.pd_ru.last_names_female)} " \
                       f"{choice(self.pd_ru.first_names_female)} " \
                       f"{choice(self.pd_ru.middle_names_female)}"
        if loc == 'en':
            if parameter == "m":
                return f"{choice(self.pd_en.first_names_male)} " \
                       f"{choice(self.pd_en.last_names)}"
            if parameter == "f":
                return f"{choice(self.pd_en.first_names_female)} " \
                       f"{choice(self.pd_en.last_names)}"

    def random_address(self, loc):
        """Randomize address from address_data"""
        if loc == 'ru':
            return f"{choice(self.ad_ru.city_names)} " \
                   f"ул.{choice(self.ad_ru.street_titles)} {randint(1, 200)}"
        if loc == 'en':
            return f"{choice(self.ad_en.states)} " \
                f"{choice(self.ad_en.street_suffixes)} Street {randint(1, 200)}"

    def random_job(self, loc):
        """Randomize job from job_data"""
        if loc == 'ru':
            return f"{choice(self.jd_ru.jobs)}"
        if loc == 'en':
            return f"{choice(self.jd_en.jobs)}"

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

    @classmethod
    def generate(cls):
        """Main method. Use it for generate data with console parameters. -h for more info."""
        generator = cls()

        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(help='This script generates fictional data about person or password. '
                                                'Available commands:')

        person_parser = subparsers.add_parser('person', help='Generate person.')

        person_parser.add_argument('localization', type=str, help='Available localizations are: ru/en.')
        person_parser.add_argument('sex', type=str, help='Can be male or female. [m/f]')
        person_parser.add_argument('num', type=int, help='Number of persons. [int]')
        person_parser.add_argument('average_age', type=int, help='Average age. [int]')

        password_parser = subparsers.add_parser('password', help='Generate person.')

        password_parser.add_argument('length', type=int, help='Length of password. It may be 8 and > ...')
        password_parser.add_argument('n', type=int, help='Number of passwords.')

        args = parser.parse_args()

        if (vars(args)):
            try:
                for _ in range(args.num):
                    print(generator.random_person(args.sex, args.localization),
                          generator.average_age(args.average_age),
                          generator.random_address(args.localization),
                          generator.random_job(args.localization),
                          generator.phone_number())
            except KeyboardInterrupt:
                sys.exit()

            except AttributeError:
                try:
                    for _ in range(args.n):
                        print(generator.password(args.length))
                except KeyboardInterrupt:
                    sys.exit()
        print('Please enter parameters. For more info use [-h].')


if __name__ == "__main__":
    Generator.generate()
