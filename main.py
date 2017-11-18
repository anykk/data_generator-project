import sys
import argparse
from generator import Generator


generator = Generator()


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='This script generates fictional data about person or password. '
                                            'Available commands:')

    person_parser = subparsers.add_parser('person', help='Generate person.')

    person_parser.add_argument('localization', type=str, help=f'Available localizations are:'
                                                              f' {generator.available_locales}')
    person_parser.add_argument('sex', type=str, help='Can be male or female. [m/f]')
    person_parser.add_argument('num', type=int, help='Number of persons. [int]')
    person_parser.add_argument('average_age', type=int, help='Average age. [int]')

    password_parser = subparsers.add_parser('password', help='Generate person.')

    password_parser.add_argument('length', type=int, help='Length of password. It may be 8 and > ...')
    password_parser.add_argument('n', type=int, help='Number of passwords.')

    return parser.parse_args()


def generate():
    """Main method. Use it for generate data with console parameters. -h for more info."""
    args = parse_args()

    if (vars(args)):
        try:
            if (args.localization in generator.available_locales):
                for _ in range(args.num):
                    print(generator.random_person(args.sex, args.localization),
                          generator.average_age(args.average_age),
                          generator.random_address(args.localization),
                          generator.random_job(args.localization),
                          generator.phone_number())
            else:
                print("Invalid localization. Please check list of available localizations by 'person -h' parameter.")
                sys.exit()

        except AttributeError:
            try:
                for _ in range(args.n):
                    print(generator.password(args.length))
            except KeyboardInterrupt:
                sys.exit()

        except KeyboardInterrupt:
            sys.exit()
    else:
        print('Please enter parameters. For more info use [-h].')


if __name__ == '__main__':
    generate()
