# https://leetcode.com/problems/merge-intervals/description/
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    answer = [intervals[0]]

    max_so_far = intervals[0][1]

    for i in range(1, len(intervals)):

        if max_so_far >= intervals[i][0]:
            max_so_far = max(max_so_far, intervals[i][1])
            answer[-1][1] = max_so_far
        else:
            answer.append(intervals[i])
            max_so_far = intervals[i][1]

    return (answer)


intervals = [[1,3],[2,6],[8,10],[15,18]]
v1 = merge(intervals)
print(v1)