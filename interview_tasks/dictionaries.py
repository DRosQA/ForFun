"""
Implement a group_by_owners function that:
- Accepts a dictionary containing the file owner name for each file name.
- Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for a dictionary:
    {'Input.txt': 'Romek', 'Code.py': 'Staszek', 'Output.txt': 'Romek'} 
the group_by_owners function should return: 
    {'Romek': ['Input.txt', 'Output.txt'], 'Staszek': ['Code.py']}.
"""


def group_by_owners(files):
    print(files)
    owners = {}
    for key, value in files.items():
        owners.setdefault(value, []).append(key)
    print(owners)
    return owners


if __name__ == '__main__':
    group_by_owners({'Input.txt': 'Romek', 'Code.py': 'Staszek', 'Output.txt': 'Romek'})
