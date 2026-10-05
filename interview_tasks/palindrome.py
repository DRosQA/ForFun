# Write an algorithm which will check if the given word is a palindrome
# (expression which sounds the same whether it's read from left to right or right to left).


def check_if_palindrome(text):
    text = text.lower()
    if len(text) >= 2:
        for i in range(1, len(text)):
            if text[i - 1] != text[len(text) - i]:
                return False
            else:
                i = i + 1
                if i > len(text) / 2:
                    return True
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
    "Madam"
]


def print_result(words_list):
    for i in words_list:
        result = check_if_palindrome(i)
        print(result)


if __name__ == '__main__':
    print_result(words)
