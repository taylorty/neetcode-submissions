class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        maxSoFar = 0
        for i, num in enumerate(nums):
            if maxSoFar >= i:
                dp[i] = i + num
            maxSoFar = max(dp[i], maxSoFar)
            if maxSoFar >= len(nums) - 1:
                return True
        return False
