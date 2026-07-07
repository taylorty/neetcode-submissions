class Solution:
    def jump(self, nums: List[int]) -> int:
        maxSoFar = 0
        dp = {} # min at i position
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            
            farthest = min(len(nums) - 1, i + nums[i])
            res = float('inf')
            for nextIndex in range(i + 1, farthest + 1):
                res = min(1 + dfs(nextIndex), res)
            dp[i] = res
            return dp[i]
        
        return dfs(0)
        # for i, num in enumerate(nums):
        #     if maxSoFar >= i:
        #         currMax = i + num

        #     maxSoFar = max(currMax, maxSoFar)
        #     if maxSoFar >= len(nums) - 1:
        #         return True
        # return False