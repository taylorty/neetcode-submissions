class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        target = sums // 2
        
        if sums % 2 != 0:
            return False
        n = len(nums)
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(nums, currSum, i):
            if i >= n or currSum < 0:
                return False
            if currSum == 0:
                return True
            if memo[i][currSum] != -1:
                return memo[i][currSum]
            memo[i][currSum] = dfs(nums, currSum - nums[i], i + 1) or dfs(nums, currSum, i + 1)
            return memo[i][currSum]
        
        return dfs(nums, target, 0)
