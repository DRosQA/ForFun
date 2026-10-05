def compare_strings(text, text2):
    # sorted() sorts strings alphabetically
    # if strings are an anagram, they will sort to an identical string
    return sorted(text) == sorted(text2)

if __name__ == '__main__':
    text = 'text'
    text2 = 'xtte'
    result = compare_strings(text, text2)
    print(f"are \'{text}\' and \'{text2}\' anagrams of each other?", result)
