# Write an algorithm which will check if the given word is a palindrome
# (expression which sounds the same whether it's read from left to right or right to left).
import string


def check_if_palindrome(text):
    # convert everything into a single string in lowercase and without punctuation
    text = "".join(str(text)).lower().replace(" ", "")
    for char in text:
        if char in string.punctuation:
            text = text.replace(char, "")
    if len(text)>0:    
        # check if string is identical to reversed string
        return text == text[::-1]
    else:
        return False

words = [
    "",
    "o",
    "wow",
    "papap",
    "oh",
    "omg",
    "meme",
    "hello",
    "Madam",
    "papap",
    "I did,. did I",
    121,
    123,
    "me em",
    ["me", "em"],
    {"me", "em"}
]


def print_palindrome_check_result(words_list):
    for word in words_list:
        result = str(check_if_palindrome(word))
        print(f"is \'{word}\' a palindrome?", result)


if __name__ == '__main__':
    print_palindrome_check_result(words)
