import string


def check_if_palindrome(arg):
    # convert everything into a single string in lowercase and without punctuation
    arg = "".join(str(arg)).lower().replace(" ", "")
    for char in arg:
        if char in string.punctuation:
            arg = arg.replace(char, "")
    if len(arg) > 1:  # making the executive decision to judge that 1-character strings are not palindromes
        # check if string is identical to reversed string
        return arg == arg[::-1]
    else:
        return False


def reverse(arg):
    newarr = []
    for item in arg:
        newarr.append((item[1], item[0]))
    print(newarr)


if __name__ == '__main__':
    text = "abba"
    test_data_palindromes = [
        (False, ''),
        (False, 'o'),
        (True, 'wow'),
        (False, 'oh'),
        (False, 'omg'),
        (False, 'meme'),
        (False, 'hello'),
        (True, 'Madam'),
        (True, 'papap'),
        (True, 'I did,. did I'),
        (True, 121),
        (False, 123),
        (True, ("me", "em")),
        (True, ["me", "em"]),
        (True, {"me", "em"})
    ]
    reverse(test_data_palindromes)
    result = check_if_palindrome(text)
    print(f"is \'{text}\' a palindrome?", result)
