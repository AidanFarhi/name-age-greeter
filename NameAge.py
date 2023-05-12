from collections import namedtuple


def age_to_calendar_year(age: int) -> int:
    """Converts an age in years to the calendar year of birth.

    Args:
        age: The age in years to find the birth year for.

    Returns:
        The calendar year of birth.
    """
    pass


def get_input() -> namedtuple:
    """Gets personal attributes from standard input and packages them into an object.

    Returns:
        A Person object containing the given name and age.
    """
    Person = namedtuple('Person', ['name', 'age'])
    name = input('What is your name? ')
    age = int(input('How old are you? '))
    return Person(name, age)


def main() -> None:
    """Main function of program."""
    name_and_age = get_input()
    print(name_and_age)


if __name__ == '__main__':
    main()
