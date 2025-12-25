
def max_sum(nums):
    global_sum = nums[0]
    curr_sum = 0
    for i in nums:
        curr_sum = curr_sum + i
        if curr_sum > global_sum:
            global_sum = curr_sum
        elif curr_sum < 0:
            curr_sum = 0
    return global_sum
    
nums = [4,-1,2,-7,3,4]
res = max_sum(nums)
print(res)