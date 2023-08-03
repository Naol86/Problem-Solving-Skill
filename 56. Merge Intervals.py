from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        Index = 1
        intervals.sort()
        while (Index < len(intervals)):
            if intervals[Index-1][1] >= intervals[Index][0]:
                intervals[Index-1][1] = intervals[Index][1] if intervals[Index -
                                                                        1][1] < intervals[Index][1] else intervals[Index-1][1]
                intervals.pop(Index)
            else:
                Index += 1
        return intervals
