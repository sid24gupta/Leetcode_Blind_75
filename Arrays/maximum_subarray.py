# https://leetcode.com/problems/maximum-subarray/description/

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6

nums = [-2,-1]
def maxSubArray(nums):
    
    if len(nums)==1:
        return nums[0]
            
    max_sum_so_far = nums[0]
    total = 0
    i  = 0
    
    while i < len(nums):

        total += nums[i]

        if total > max_sum_so_far:
            max_sum_so_far = total
        
        if total < 0:
            total = 0
        
        i += 1

    return max_sum_so_far



v1 = maxSubArray(nums)
print(v1)