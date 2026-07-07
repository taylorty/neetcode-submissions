class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob2(nums[:-1]), self.rob2(nums[1:]))

    def rob2(self, nums: List[int]):
        n = len(nums)
        if not n:
            return 0
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            # if i == nums - 1:

            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]