import sys
import argparse

from random import choice as choice
from random import randint as randint
from random import randrange as randrange
from random import shuffle as shuffle

from data_generator.data import pds, available_locales


class Generator(object):
    """A class, that generates fictional data"""

    def __init__(self):
        """Initialize the class object and collect all the data together
        pds - personal data
        available_locales - locales, that are available now"""
        self.pds = pds
        self.available_locales = available_locales

    def random_person(self, parameter, loc):
        """Depending on parameter randomize different persons"""
        if parameter == "m":
            return f"{choice(self.pds[loc].person.first_names_male)} " \
                   f"{choice(self.pds[loc].person.last_names_male)}"
        if parameter == "f":
            return f"{choice(self.pds[loc].person.first_names_female)} " \
                   f"{choice(self.pds[loc].person.last_names_female)}"

    def random_address(self, loc):
        """Randomize address from address_data"""
        return f"{choice(self.pds[loc].address.city_names)} " \
               f"{choice(self.pds[loc].address.street_titles)} {randint(1, 200)}"

    def random_job(self, loc):
        """Randomize job from job_data"""
        return f"{choice(self.pds[loc].jobs)}"

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

    @staticmethod
    def parse_args():
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

        return parser.parse_args()

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

        args = Generator.parse_args()

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
        else:
            print('Please enter parameters. For more info use [-h].')


if __name__ == "__main__":
    Generator.generate()
