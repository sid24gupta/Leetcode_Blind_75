# https://leetcode.com/problems/subsets/
# 78. Subsets
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
from typing import List

nums = [1,2,3]
def subsets(nums: List[int]) -> List[List[int]]:
    ans, sol = [], []

    def backtrack(i):
        if i == len(nums):
            ans.append(sol[:])
            return

        # dont pick
        backtrack(i + 1)

        # pick it
        sol.append(nums[i])
        backtrack(i+1)
        sol.pop()

    backtrack(0)
    return ans

v1 = subsets(nums)
print(v1)