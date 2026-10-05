def reverse_string(text):
    # string slicing -> str[start:end:step]
    # this is take string from beginning (default), to end (default), 
    # reversing the characters without skipping any
    return text[::-1]

if __name__ == '__main__':
    text = 'testingTheReverse'
    result = reverse_string(text)
    print(result)
