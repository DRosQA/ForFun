def reverse_string(arg):
    # string slicing -> str[start:end:step]
    # this is take string from beginning (default), to end (default),
    # reversing the characters without skipping any
    return str(arg)[::-1]


if __name__ == "__main__":
    print("Reversing a string.", end=" ")
    text = input("Enter a string to reverse:\n")
    # text = "string To Test"
    result = reverse_string(text)
    print(f"'{text}' reversed is '{result}'")
