import unittest
import interview_tasks.palindrome as palindrome


class TestPalindrome(unittest.TestCase):
    words_with_palindrome_correctness = {
        "": False,
        "o": False,
        "wow": True,
        "oh": False,
        "omg": False,
        "meme": False,
        "hello": False,
        "Madam": True,
        "papap": True,
        "I did,. did I": True,
        121: True,
        123: False,
        "me em": True,
        # ["me", "em"]: True,
        # {"me", "em"}: True
    }

    def testPalindrome(self, cases=words_with_palindrome_correctness):
        for case, correctness in cases.items():
            expected = correctness
            actual = palindrome.check_if_palindrome(case)
            if expected == actual:
                print(str(case) + ': pass')
            else:
                print(str(case) + ': fail')


if __name__ == "__main__":
    unittest.main()
