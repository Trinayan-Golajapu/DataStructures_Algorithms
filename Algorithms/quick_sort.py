def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[-1]
    left = []
    right = []

    for i in range(len(nums)-1):
        if nums[i] <= pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


nums = [10,7,8,9,1,5]
res = quick_sort(nums)
print(res)