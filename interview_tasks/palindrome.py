# Write an algorithm which will check if the given word is a palindrome
# (expression which sounds the same whether it's read from left to right or right to left).


def check_if_palindrome(text):
    for i in range(1, len(text)):
        if text[i - 1] != text[len(text) - i]:
            print("'" + text + "' is not a palindrome")
            break
        else:
            i = i + 1
            if i > len(text) / 2:
                print("'" + text + "' is a palindrome")
                break


if __name__ == '__main__':
    check_if_palindrome("papap")
