# https://leetcode.com/problems/3sum/description/
# 15. 3Sum

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:

    ans = set()
    nums.sort()
    for i in range(len(nums)-2):

        l = i + 1
        r = len(nums)-1

        while l < r:
                
            if nums[i] + nums[l] + nums[r] == 0:
                ans.add((nums[i],nums[l],nums[r]))
                l += 1
                r -= 1
            
            elif nums[i] + nums[l] + nums[r] > 0 :
                r -= 1

            else:
                l += 1

    return [list(i) for i in ans]



nums = [-1,0,1,2,-1,-4]
v1 = threeSum(nums)
print(v1)