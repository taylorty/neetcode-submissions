class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {} # (index, total) -> # of ways
        def dfs(nums, target, curr, i):
            if target == curr and i == len(nums):
                return 1

            if i >= len(nums):
                return 0
            if (i, curr) in memo:
                return memo[(i, curr)]
            memo[(i, curr)] = dfs(nums, target, curr - nums[i], i + 1) + dfs(nums, target, curr + nums[i], i + 1)
            return memo[(i, curr)]

        return dfs(nums, target, 0, 0)