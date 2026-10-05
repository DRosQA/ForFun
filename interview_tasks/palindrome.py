import string

def check_if_palindrome(text):
    # convert everything into a single string in lowercase and without punctuation
    text = "".join(str(text)).lower().replace(" ", "")
    for char in text:
        if char in string.punctuation:
            text = text.replace(char, "")
    if len(text) > 1:     # making the executive decision to judge that 1-character strings are not palindromes
        # check if string is identical to reversed string
        return text == text[::-1]
    else:
        return False


if __name__ == '__main__':
    text = "abba"
    result = check_if_palindrome(text)
    print(f"is \'{text}\' a palindrome?", result)
