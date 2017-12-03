import sys
import argparse
from generator import Generator
from data.utility import LocalizationNotFoundError, WrongLocalizationError


def main(data="data"):
    """Main method. Use it for generate data with console parameters. -h for more info."""
    generator = Generator(data, data)
    args = parse_args(generator)

    if 'length' in args:
        try:
            for _ in range(args.n):
                print(generator.password(args.length))
        except KeyboardInterrupt:
            sys.exit()
    else:
        if args.localization not in generator.wrong_localizations:
            raise LocalizationNotFoundError(f"Undefined localization: '{args.localization}'. Please check data folder.")
        if generator.wrong_localizations[args.localization]:
            raise WrongLocalizationError(f"Something wrong with following files: "
                                         f"{generator.wrong_localizations[args.localization]} "
                                         f"in '{args.localization}' localization. Please check it in data folder.")
        for _ in range(args.num):
            print(generator.random_person(args.sex, args.localization),
                  generator.average_age(args.average_age),
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
    person_parser.add_argument('sex', type=str, help='Can be male or female. [m/f]')
    person_parser.add_argument('num', type=int, help='Number of persons. [int]')
    person_parser.add_argument('average_age', type=int, help='Average age. [int]')

    password_parser = subparsers.add_parser('password', help='Generate password.')

    password_parser.add_argument('length', type=int, help='Length of password. It may be 8 and > ...')
    password_parser.add_argument('n', type=int, help='Number of passwords.')

    return parser.parse_args(['']) if len(sys.argv) == 1 else parser.parse_args()


if __name__ == "__main__":
    main()
