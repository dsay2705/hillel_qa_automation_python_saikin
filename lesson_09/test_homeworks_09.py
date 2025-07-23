import unittest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from homeworks import sum_string_numbers, find_substring, get_strings

class TestSumStringNumbers(unittest.TestCase):
    """Tests for the sum_string_numbers function from homework_08."""

    def test_all_numbers(self):
        self.assertEqual(sum_string_numbers("1,2,3,4"), 10)
        self.assertEqual(sum_string_numbers("1,2,3,4,50"), 60)

    def test_non_numeric_prefix(self):
        self.assertEqual(sum_string_numbers("qwerty1,2,3"), "Не можу це зробити")

    def test_non_numeric_postfix(self):
        self.assertEqual(sum_string_numbers("1,2,4,abc"), "Не можу це зробити")

    def test_empty_string(self):
        self.assertEqual(sum_string_numbers(""), "Не можу це зробити")

    def test_negative_numbers(self):
        self.assertEqual(sum_string_numbers("-1,-2,3"), 0)

    def test_spaces_between_numbers(self):
        self.assertEqual(sum_string_numbers("1, 2,3"), 6)

class TestFindSubstring(unittest.TestCase):
    """Tests for the find_substring function from homework_07."""

    def test_substring_present(self):
        self.assertEqual(find_substring("Hello, world!", "world"), 7)
        self.assertEqual(find_substring("abcdef", "cd"), 2)
        self.assertEqual(find_substring("abcabcabc", "bca"), 1)

    def test_substring_not_present(self):
        self.assertEqual(find_substring("Hello, world!", "python"), -1)
        self.assertEqual(find_substring("abcdef", "gh"), -1)

    def test_empty_substring(self):
        self.assertEqual(find_substring("abcdef", ""), 0)

    def test_empty_string(self):
        self.assertEqual(find_substring("", "abc"), -1)

    def test_both_empty(self):
        self.assertEqual(find_substring("", ""), 0)

    def test_substring_at_start(self):
        self.assertEqual(find_substring("abcdef", "abc"), 0)

    def test_substring_at_end(self):
        self.assertEqual(find_substring("abcdef", "ef"), 4)

class TestGetStrings(unittest.TestCase):
    """Tests for the get_strings function from homework_06."""

    def test_only_strings(self):
        self.assertEqual(get_strings(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_no_strings(self):
        self.assertEqual(get_strings([1, 2, 3, False, None]), [])

    def test_empty_list(self):
        self.assertEqual(get_strings([]), [])

    def test_all_types(self):
        self.assertEqual(
            get_strings(['str', 1, 2.2, False, 'another', {}, [], 'last']),
            ['str', 'another', 'last']
        )

    def test_unicode_strings(self):
        self.assertEqual(get_strings(['тест', 123, '😊']), ['тест', '😊'])

    def test_nested_lists(self):
        self.assertEqual(get_strings(['a', ['b'], 'c']), ['a', 'c'])

    def test_dict_in_list(self):
        self.assertEqual(get_strings(['a', {'b': 1}, 'c']), ['a', 'c'])

    def test_boolean_strings(self):
        self.assertEqual(get_strings(['True', True, 'False', False]), ['True', 'False'])

if __name__ == '__main__':
    unittest.main()