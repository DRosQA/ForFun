def reverse_string(arg):
    # string slicing -> str[start:end:step]
    # this is take string from beginning (default), to end (default), 
    # reversing the characters without skipping any
    return str(arg)[::-1]


if __name__ == '__main__':
    test_string = 'string To Test'
    result = reverse_string(test_string)
    print(f"\'{test_string}\' reversed is \'{result}\'")
