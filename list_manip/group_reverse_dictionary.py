def group_by_values(arg):
    values = {}
    for key, value in arg.items():
        # setdefault() checks it key exists, if not, adds it with the specified value
        # we append so that the resulting value is an array
        values.setdefault(value, []).append(key)
    return values


def input_dictionary():
    keys_input = input("How many dictionary entries would you like to input?\n")
    try:
        keys_amount = int(keys_input)
    except ValueError:
        print("Input keys amount is not an integer.", end=" ")
        return {}
    print("Enter key-value pairs:")
    constructed_dict = {}
    for nameValuePair in range(keys_amount):
        key = str(input("Key: "))
        val = str(input("Value: "))
        constructed_dict[key] = val
    return constructed_dict


if __name__ == "__main__":
    print("Grouping dictionary entries by repeated values. Enter dictionary to change.", end=' ')
    example_dictionary = input_dictionary()
    # example_dictionary = {
    #     "Input.txt": "Romek",
    #     "Code.py": "Staszek",
    #     "Output.txt": "Romek",
    # }
    result = group_by_values(example_dictionary)
    if result:
        print(
            f"Dictionary {example_dictionary} grouped by values is {result}"
        )
