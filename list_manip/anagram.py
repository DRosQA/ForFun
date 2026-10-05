def check_for_anagrams(args):
    # sorted() sorts strings alphabetically
    # if strings are an anagram, they will sort to an identical string list
    if len(args) > 1:
        # converting to list so it takes sets
        return all(sorted(str(x)) == sorted(str(list(args)[0])) for x in args)
    else:
        print("argument list should have more than one element to properly test for anagrams")
        return False


if __name__ == '__main__':
    text_list = ['text', 'xtte', 'ttex']
    result = check_for_anagrams(text_list)
    print(f"are {text_list} all anagrams of each other?", result)
