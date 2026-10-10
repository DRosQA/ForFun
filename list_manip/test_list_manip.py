import unittest
from typing import ClassVar

import list_manip.group_reverse_dictionary as dictionary_manip
from list_manip import anagram, missing_number, two_sum


class TestListManip(unittest.TestCase):
    test_data_anagram: ClassVar[list[tuple]] = [
        (["text", "xtte", "ttex"], True),
        (["arg", "xtte", "ttex"], False),
        (["car", "arc"], True),
        ([123, 321], True),
        ("single", False),
        (("me", "em"), True),
        (["me", "em"], True),
        ({"me", "em"}, True),
    ]

    test_data_group_dict: ClassVar[list[dict[str, str]]] = [
        (
            {"Input.txt": "Romek", "Code.py": "Staszek", "Output.txt": "Romek"},
            {"Romek": ["Input.txt", "Output.txt"], "Staszek": ["Code.py"]},
        ),
        (
            {"Lorem": "text", "Cupcake": "sweet", "Dessert": "sweet", "Ipsum": "text"},
            {"text": ["Lorem", "Ipsum"], "sweet": ["Cupcake", "Dessert"]},
        ),
        ({"single": "element"}, {"element": ["single"]}),
        ({1234: "mixed"}, {"mixed": [1234]}),
    ]
    test_data_missingno: ClassVar[list[tuple]] = [
        ([1, 2, 4, 5, 7, 8, 6], 3),
        ([1, 2, 4, 5, 7, 8, 6, 3], 9),
        ([2, 4, 5, 7, 3, 6], 1),
        ([3, "test", "strings"], False),
    ]
    test_data_twosum: ClassVar[list[tuple]] = [
        ([0, -1, 2, -3, 1], 1, {2, -1}),
        ([0, -1, 2, -3, 1], 15, {}),
        ([2, -13, 21, -3, 11], 18, {21, -3}),
        ([0, -1, 2, -3, 1, "test"], 15, False),
    ]

    def test_anagrams(self, cases=None):
        if cases is None:
            cases = self.test_data_anagram
        for test_data, expected_result in cases:
            self.assertEqual(
                expected_result,
                anagram.check_for_anagrams(test_data),
                f"test case for '{test_data}' failed",
            )

    def test_group_dict_reverse(self, cases=None):
        if cases is None:
            cases = self.test_data_group_dict
        for test_data, expected_result in cases:
            self.assertEqual(
                expected_result,
                dictionary_manip.group_by_values(test_data),
                f"test case for '{test_data}' failed",
            )

    def test_missing_no(self, cases=None):
        if cases is None:
            cases = self.test_data_missingno
        for test_data, expected_result in cases:
            self.assertEqual(
                expected_result,
                missing_number.find_missing_number(test_data),
                f"test case for '{test_data}' failed",
            )

    def test_twosum(self, cases=None):
        if cases is None:
            cases = self.test_data_twosum
        for test_data, target_sum, expected_result in cases:
            self.assertEqual(
                expected_result,
                two_sum.find_two_sum(test_data, target_sum),
                f"test case for '{test_data}' failed",
            )


if __name__ == "__main__":
    unittest.main()
