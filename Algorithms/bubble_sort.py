nums = [5,6,3,1,9]

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(0,len(nums)-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums


sorted_nums = bubble_sort(nums)
print(sorted_nums)