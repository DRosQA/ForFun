# Write an algorithm which will check if the given word is a palindrome
# (expression which sounds the same whether it's read from left to right or right to left).
import string


def check_if_palindrome(text):
    # convert everything into a single string in lowercase and without punctuation
    text = str(text)
    for i in text:
        if i in string.punctuation:
            text = text.replace(i, "")
    text = ''.join(text)
    text = text.lower().replace(" ", "")
    # check for edge cases like empty strings and short words
    if len(text) >= 2:
        # compare character by character
        for i in range(1, len(text)):
            # if characters don't match, exit
            if text[i - 1] != text[len(text) - i]:
                return False
            else:
                # if the characters match, continue checking
                i = i + 1
                # exit after reaching halfway (to not double-check the same pairs)
                if i > len(text) / 2:
                    return True
    else:
        return False
#         depends on your definition of palindrome; does it need to be a word/sentence? or just a string of characters?
#         if any string of characters 'counts' then change to:
#         return True


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
        print("'", word, "'" + " is a palindrome: " + result)


if __name__ == '__main__':
    print_palindrome_check_result(words)
