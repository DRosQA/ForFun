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


if __name__ == '__main__':
    text = "abba"
    result = check_if_palindrome(text)
    print(f"is \'{text}\' a palindrome?", result)
