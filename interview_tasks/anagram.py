def compare_strings(*args):
        # sorted() sorts strings alphabetically
        # if strings are an anagram, they will sort to an identical string list
        if len(args)>1:
            return all(sorted(x) == sorted(args[0]) for x in args)
        else:
            print("Argument should have more than one element to properly test for anagrams!")
            return False

if __name__ == '__main__':
    text_list = ['text', 'xtte', 'ttex']
    result = compare_strings(*text_list)
    print(f"are {text_list} all anagrams of each other?", result)
