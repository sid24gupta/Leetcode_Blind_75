# https://leetcode.com/problems/product-of-array-except-self/description/
# 238. Product of Array Except Self
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
        
    prefix , postfix = 1, 1

    answer = [0]*len(nums)

    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]

    for i in range(len(nums)-1,-1,-1):

        answer[i] *= postfix
        postfix *= nums[i]

    return answer


nums = [1,2,3,4]
v1  = productExceptSelf(nums)
print(v1)