# https://leetcode.com/problems/insert-interval/description/
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

    intervals.append(newInterval)
    intervals.sort()

    max_so_far = intervals[0][1]
    answer = [intervals[0]]

    for i in range(1, len(intervals)):

        if max_so_far >= intervals[i][0]:
            max_so_far = max(max_so_far, intervals[i][1])
            answer[-1][1] = max_so_far
        else:
            answer.append(intervals[i])
            max_so_far = intervals[i][1]

    return answer

intervals = [[1,3],[6,9]]
newInterval = [2,5]
v1 = insert(intervals,newInterval)
print(v1)