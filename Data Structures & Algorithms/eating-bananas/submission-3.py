class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canFinished(speed):
            hour = 0
            for pile in piles:
                hour += math.ceil(1.0 * pile / speed)
            return hour

        i = 1
        j = max(piles)
        result = j
        while i < j:
            m = (i + j) // 2
            hour = canFinished(m)
            if hour <= h:
                result = m
                j = m
            else:
                i = m + 1
        return result