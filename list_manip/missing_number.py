def find_missing_number(array):
    # for item in array:
    #     try:
    #         int(item)
    #     except:
    #         print("Argument list contains a non-integer item.", end="")
    #         return False

    n = len(array) + 1
    xor_array = 0
    xor_numbers = 0

    # xor -> convert to binary and compare, so n xor x = is n and x different?
    # then write back to binary and convert to integer
    # 2 xor 3 = 10 (binary 2) compared to 11 (binary 3), which results in 01 (binary 1)
    # letting us know they're not the same
    # xor is associative and commutative -> order of operations doesn't matter, (x ^ z) ^ c = (c ^ x) ^ z
    # as such, if two arrays are identical, their cumulative xor will be the same
    # as such, the difference between those xors will be the bits that are different, i.e. the missing number

    # XOR all array elements - will tell us what numbers ARE in the array
    for i in range(len(array)):
        try:
            array[i] = int(array[i])
            xor_array ^= array[i]
        except ValueError:
            print("Argument list contains a non-integer item.", end=" ")
            return False
    # XOR all numbers from 1 to n - will tell us what numbers SHOULD be in the array
    for i in range(1, n + 1):
        xor_numbers ^= int(i)

    # Missing number is the xor of xor_numbers and xor_array
    return xor_numbers ^ xor_array


if __name__ == "__main__":
    print("Finding a missing number in an array of consecutive primary numbers.", end=' ')
    numbers_array = [x for x in input("Enter numbers to check, separated by spaces: \n").strip().split(' ')]
    # numbers_array = [1, 2, 4, 5, 7, 8, 6]
    result = find_missing_number(numbers_array)
    if result > len(numbers_array):
        print(f"{numbers_array} contains all numbers up to", len(numbers_array))
    elif isinstance(result, int) and not isinstance(result, bool):
        print(f"The missing number in {numbers_array} is", result)
    else:
        print("The provided data cannot be checked for a missing number.")
