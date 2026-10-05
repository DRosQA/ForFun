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
  # must be sorted for binary search to work
    array.sort()

    for i in range(len(array)):
        target_number = target_sum - array[i]

        # Use binary search to find the matching number to make the target sum
        if binary_search(array, target_number):
            return [array[i], target_number]
            
    # If no pair is found in entire array
    return []
  	
if __name__ == "__main__":
    numbers_list = [0, -1, 2, -3, 1]
    target_sum = 1

    if not find_two_sum(numbers_list, target_sum):
        print("Did not find any two numbers within given array to sum to", target_sum)
    else:
        print(f"From the given array of {numbers_list}, {find_two_sum(numbers_list, target_sum)[0]} and {find_two_sum(numbers_list, target_sum)[1]} sum to the target of {target_sum}")
        
