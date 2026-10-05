def group_by_values(arg):
    values = {}
    for key, value in arg.items():
        # setdefault() checks it key exists, if not, adds it with the specified value
        # we append so that the resulting value is an array
        values.setdefault(value, []).append(key)
    return values


if __name__ == '__main__':
    example_dictionary = {'Input.txt': 'Romek', 'Code.py': 'Staszek', 'Output.txt': 'Romek'}
    print(group_by_values(example_dictionary))
