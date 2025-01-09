# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# 33. Search in Rotated Sorted Array
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

from typing import List 

def search(nums: List[int], target: int) -> int:
    
    low = 0
    high = len(nums)-1

    while low <= high:

        mid = int((low+high)/2)

        if nums[mid] == target:
            return mid
        
        if nums[mid] >= nums[low]:

            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    
    return -1


nums = [4,5,6,7,0,1,2]
target = 3
v1 = search(nums,target)
print(v1)