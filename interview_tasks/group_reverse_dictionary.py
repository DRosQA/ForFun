def group_by_values(dict):
    values = {}
    for key, value in dict.items():
        # setdefault() checks it key exists, if not, adds it with the specified value
        # we append so that the resulting value is an array
        values.setdefault(value, []).append(key)
    return values


example_dictionary = {'Input.txt': 'Romek', 'Code.py': 'Staszek', 'Output.txt': 'Romek'}

if __name__ == '__main__':
    print(group_by_values(example_dictionary))

