# https://leetcode.com/problems/maximum-product-subarray/
# 152. Maximum Product Subarray

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
from typing import List

def maxProduct(nums: List[int]) -> int:

    maxi = -float('inf')
    prefix = 1
    postfix = 1

    for i in range(len(nums)):

        if postfix == 0:
            postfix = 1
        
        if prefix == 0:
            prefix = 1

        prefix *= nums[i]
        postfix *= nums[len(nums)-i-1]

        maxi = max(maxi,max(prefix,postfix))

    return maxi

nums = [-2,0,-1]
v1 = maxProduct(nums)
print(v1)