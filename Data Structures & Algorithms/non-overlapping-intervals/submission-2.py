class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            if start < prevEnd:
                res += 1
                prevEnd = min(intervals[i][1], prevEnd)
            else:
                prevEnd = intervals[i][1]
        return res