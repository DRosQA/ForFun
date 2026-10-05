import unittest
from string_manip import palindrome, reverse_string


class TestStringManip(unittest.TestCase):
    test_data_palindromes = [
        ('', False),
        ('o', False),
        ('wow', True),
        ('oh', False),
        ('Madam', True),
        ('I did,. did I', True),
        (121, True),
        (123, False),
        (('me', 'em'), True),
        (['me', 'em'], True),
        ({'me', 'em'}, True),
        ('incorrect', False)
    ]

    test_data_reverse = [
        ('', ''),
        ('o', 'o'),
        ('omg', 'gmo'),
        ('meme', 'emem'),
        ('hello', 'olleh'),
        ('Madam', 'madaM'),
        ('I did,. did I', 'I did .,did I'),
        (123, '321')
    ]

    def test_palindromes(self, cases=test_data_palindromes):
        for test_data, expected_result in cases:
            self.assertEqual(expected_result, palindrome.check_if_palindrome(test_data),
                             f"test case for \'{test_data}\' failed")

    def test_reverse(self, cases=test_data_reverse):
        for test_data, expected_result in cases:
            self.assertEqual(expected_result, reverse_string.reverse_string(test_data),
                             f"test case for \'{test_data}\' failed")


if __name__ == "__main__":
    unittest.main()
