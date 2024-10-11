# https://leetcode.com/problems/two-sum/description/
# 1. Two Sum
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Approach:
# 1) If brute force is applied = Use two loops and check the sum of two elements. The time complexity
# will increase to O(n^2). To remove this dictionary is used, which keep track of the element postion
# 2) Create a dictionary to check whether the difference of the element and target is present or not.

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:

    lookup = {} # creating a lookup dictionary to store the elements positions

    for i in range(len(nums)):

        diff = target - nums[i]

        if diff not in lookup: # checking whether difference is present in dictionary 
            lookup[nums[i]] = i

        else:
            return [lookup[diff],i]


nums = [2,7,11,15]
target = 9

# returning the result into result variable
result = twoSum(nums,target)
print(result)