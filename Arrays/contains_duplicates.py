# https://leetcode.com/problems/contains-duplicate/description/
# 217. Contains Duplicate
# Input: nums = [1,2,3,1]
# Output: true
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
        
    lookup = {}

    for i in nums:
        if i in lookup:
            return 1
        else:
            lookup[i] = 1
    
    return 0

nums = [1,2,3,1]
v1 = containsDuplicate(nums)
print(v1)