from unittest import TestCase
from datetime import date
from io import StringIO
from unittest.mock import patch
from NameAge import (
    get_person_info,
    get_birth_year_from_age,
    generate_greeting,
    main
)


class TestNameAge(TestCase):
    def test_get_person_info(self):
        with patch('sys.stdin', StringIO('John\n30\n')):
            expected_person = ('John', 30)
            actual_person = get_person_info()
            self.assertEqual(expected_person, actual_person)

    def test_get_birth_year_from_age(self):
        expected_birth_year = date.today().year - 30
        actual_birth_year = get_birth_year_from_age(30)
        self.assertEqual(expected_birth_year, actual_birth_year)

    def test_generate_greeting(self):
        expected_greeting = "\nHello John! You were born in 1990."
        actual_greeting = generate_greeting("John", 1990)
        self.assertEqual(expected_greeting, actual_greeting)

    @patch('builtins.input', side_effect=['John', '30'])
    def test_main(self, mock_input):
        year = date.today().year - 30
        expected_output = f"\nHello John! You were born in {year}."
        with StringIO() as output:
            with patch('sys.stdout', new=output):
                main()
                actual_output = output.getvalue()
                self.assertEqual(expected_output, actual_output)
