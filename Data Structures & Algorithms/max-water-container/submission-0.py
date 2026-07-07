class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        res = 0
        while i < j:
            res = max(res, min(heights[i], heights[j]) * (j - i))
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1
        return res