import argparse
import sys

from generator import Generator
from utility import LocalizationNotFoundError


def main():
    """Main method. Use it for generate data with console parameters. -h for more info."""
    generator = Generator()
    args = parse_args(generator)

    if 'length' in args:
        try:
            for _ in range(args.n):
                print(generator.password(args.length))
        except KeyboardInterrupt:
            sys.exit()
    else:
        if args.localization not in generator.pds:
            raise LocalizationNotFoundError(args.localization, generator.data_folder)
        for _ in range(args.count):
            print(generator.random_person(args.gender, args.localization),
                  generator.average_age(args.age),
                  generator.random_address(args.localization),
                  generator.random_job(args.localization),
                  generator.phone_number())


def parse_args(generator):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='This script generates fictional data about person or password. '
                                            'Available commands:')

    person_parser = subparsers.add_parser('person', help='Generate person.')

    person_parser.add_argument('localization', type=str, help=f'Localization, you can choose from:'
                                                              f'{generator.available_locales}')
    person_parser.add_argument('gender', type=str, help='Can be male or female. [m/f]')
    person_parser.add_argument('count', type=int, help='Count of persons. [int]')
    person_parser.add_argument('age', type=int, help='Average age. [int]')

    password_parser = subparsers.add_parser('password', help='Generate password.')

    password_parser.add_argument('length', type=int, help='Length of password. It may be 8 and > ...')
    password_parser.add_argument('n', type=int, help='Number of passwords.')

    return parser.parse_args(['']) if len(sys.argv) == 1 else parser.parse_args()


if __name__ == "__main__":
    main()
