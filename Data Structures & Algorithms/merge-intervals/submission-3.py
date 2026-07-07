class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        i = 0
        res = []
        prev = intervals[i]
        i += 1
        while i < len(intervals):
            if prev[1] < intervals[i][0]:
                res.append(prev)
                prev = intervals[i]
                
            else:
                prev[0] = min(prev[0], intervals[i][0])
                prev[1] = max(prev[1], intervals[i][1])
            i += 1
        res.append(prev)
        return res