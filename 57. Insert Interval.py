class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        Index = 0
        if len(intervals) == 0:
            return [newInterval]
        for i in range(len(intervals)):
            if (newInterval[0] <= intervals[i][1]):
                Index = i
                if intervals[i][0] > newInterval[0]:
                    intervals.insert(i, newInterval)
                else:
                    intervals.insert(i+1, newInterval)
                break
            if i == len(intervals)-1:
                intervals.insert(i+1, newInterval)
        while (Index < len(intervals)-1):
            if intervals[Index][1] >= intervals[Index+1][0]:
                intervals[Index][1] = intervals[Index+1][1] if intervals[Index + 1][1] > intervals[Index][1] else intervals[Index][1]
                intervals.pop(Index+1)
            else:
                break
        return intervals
