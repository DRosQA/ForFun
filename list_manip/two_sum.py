def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # target found
        if array[mid] == target:
            return True
        # target is bigger than mid -> go right
        elif array[mid] < target:
            left = mid + 1
        # target is smaller than mid -> go left
        else:
            right = mid - 1

    # if we reach end of array without finding a target, return False
    return False


def find_two_sum(array, target_sum):

    for i in range(len(array)):
        try:
            array[i] = int(array[i])
        except ValueError:
            print("Argument list contains a non-integer item.", end=" ")
            return False
    try:
        target_sum = int(target_sum)
    except ValueError:
        print("Target sum is not an integer.", end=" ")
        return False

    # must be sorted for binary search to work
    array.sort()

    for i in range(len(array)):
        target_number = target_sum - array[i]

        # Use binary search to find the matching number to make the target sum_target
        if binary_search(array, target_number):
            return {array[i], target_number}

    # If no pair is found in entire array
    return {}


if __name__ == "__main__":
    print("Finding a pair of numbers that add to a target sum.", end=" ")
    numbers_array = [x for x in input("Enter numbers to check, separated by spaces: \n").strip().split(' ')]
    # numbers_array = [0, -1, 2, -3, 1]
    sum_target = input("Enter the target sum: \n")

    result = find_two_sum(numbers_array, sum_target)
    if result:
        print(
            f"From the given array of {numbers_array}, "
            f"{
                str(result)
                .replace('{', '')
                .replace('}', '')
                .replace(',', ' and')
            }"
            f" sum to the target of {sum_target}"
        )
    else:

        print(
            f"Did not find any two numbers within given array to sum_target to {sum_target}"
        )
