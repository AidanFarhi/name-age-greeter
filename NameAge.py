from collections import namedtuple
from datetime import date


def age_to_calendar_year(age: int) -> int:
    """Calculates a calendar year based on given age.

    Args:
        age: The age in years to find the birth year for.

    Returns:
        The calendar year of birth.
    """
    current_year = date.today().year
    return current_year - age


def get_input() -> namedtuple:
    """Gets personal attributes from standard input and packages them into an object.

    Returns:
        A Person object containing the attributes.
    """
    Person = namedtuple('Person', ['name', 'age'])
    name = input('What is your name? ')
    age = int(input('How old are you? '))
    return Person(name, age)


def main() -> None:
    """Main function of program."""
    person = get_input()
    birth_year = age_to_calendar_year(person.age)
    print(f'\nHello {person.name}! You were born in {birth_year}.', end='')


if __name__ == '__main__':
    main()
