def find_missing_number(array):
    for item in array:
        if isinstance(item, int) and not isinstance(item, bool):
            continue
        else:
            print('Argument list contains non-integer item.')
            return False

    n = len(array) + 1
    xor_array = 0
    xor_numbers = 0

    # xor -> convert to binary and compare, so n xor x = is n and x different?
    # then write back to binary and convert to integer
    # 2 xor 3 = 10 (binary 2) compared to 11 (binary 3), which results in 01 (binary 1)
    # letting us know they're not the same
    # xor is associative and commutative -> order of operations doesn't matter, (x ^ z) ^ c = (c ^ x) ^ z
    # as such, if two arrays are identical, their cumulative xor will the the same
    # as such, the difference between those xors will be the bits that are different, i.e. the missing number

    # XOR all array elements - will tell us what numbers ARE in the array
    for i in range(n - 1):
        xor_array ^= array[i]

    # XOR all numbers from 1 to n - will tell us what numbers SHOULD be in the array
    for i in range(1, n + 1):
        xor_numbers ^= i

    # Missing number is the xor of xor_numbers and xor_array
    return xor_numbers ^ xor_array


if __name__ == '__main__':
    numbers_array = [1, 2, 4, 5, 7, 8, 6]
    result = find_missing_number(numbers_array)
    if result > len(numbers_array):
        print('given array contains all numbers up to', len(numbers_array))
    else:
        print('the missing number in the given array is', result)
