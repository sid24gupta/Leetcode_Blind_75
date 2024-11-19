# https://leetcode.com/problems/container-with-most-water/description/
# 11. Container With Most Water
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.
from typing import List

def maxArea(height: List[int]) -> int:
    
    result = 0
    l = 0
    r = len(height) - 1

    while l<r:

        area = (r-l) * min(height[l], height[r])
        result = max(result, area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return result


height = [1,8,6,2,5,4,8,3,7]
v1 = maxArea(height)
print(v1)