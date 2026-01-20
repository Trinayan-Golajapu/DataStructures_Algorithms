def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid          # target found
        elif arr[mid] < target:
            left = mid + 1      # search right half
        else:
            right = mid - 1     # search left half

    return -1  # target not found

arr = [1, 3, 5, 7, 9, 11]
target = 7

print(binary_search(arr, target))

