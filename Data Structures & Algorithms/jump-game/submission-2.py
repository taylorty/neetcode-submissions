class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxSoFar = 0
        for i, num in enumerate(nums):
            if maxSoFar >= i:
                currMax = i + num
            maxSoFar = max(currMax, maxSoFar)
            if maxSoFar >= len(nums) - 1:
                return True
        return False
