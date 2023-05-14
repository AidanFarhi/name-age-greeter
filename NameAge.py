from collections import namedtuple
from datetime import date
from typing import Tuple


def get_person_info() -> Tuple[str, int]:
    """Gets personal info from standard input and stores it in an object.

    Returns:
        A person's info.
    """
    Person = namedtuple('Person', ['name', 'age'])
    name = input('What is your name? ')
    age = int(input('How old are you? '))
    return Person(name, age)


def get_birth_year_from_age(age: int) -> int:
    """Calculates a calendar year based on given age.

    Args:
        age: The age in years to find the birth year for.

    Returns:
        The calendar year of birth.
    """
    return date.today().year - age


def generate_greeting(name: str, year: int) -> str:
    """Generates a greeting string.

    Args:
        name: The name to be used in the greeting.
        year: The year to be used in the greeting.

    Returns:
        A greeting including personal info.
    """
    return f'\nHello {name}! You were born in {year}.'


def main() -> None:
    """Main function of program."""
    person = get_person_info()
    birth_year = get_birth_year_from_age(person.age)
    greeting = generate_greeting(person.name, birth_year)
    print(greeting)


if __name__ == '__main__':
    main()
