def check_for_anagrams(args):
    # sorted() sorts strings alphabetically
    # if strings are an anagram, they will sort to an identical string list
    if len(args) > 1:
        # converting to list so it takes sets
        return all(sorted(str(x)) == sorted(str(list(args)[0])) for x in args)
    else:
        print(
            "Argument list should have more than one element to properly test for anagrams."
        )
        return False


if __name__ == "__main__":
    print("Checking for anagrams in text.", end=' ')
    # text_list = ["text", "xtte", "ttex"]
    text_list = [str(x) for x in input("Enter text to check, separated by spaces: \n").split(' ')]
    result = check_for_anagrams(text_list)
    if result:
        print(f"\nAre {text_list} all anagrams of each other?", result)
