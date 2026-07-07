class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(nums, target, curr, i):
            
            if target == curr and i == len(nums):
                return 1

            if i >= len(nums):
                return 0

            return dfs(nums, target, curr - nums[i], i + 1) + dfs(nums, target, curr + nums[i], i + 1)

        return dfs(nums, target, 0, 0)