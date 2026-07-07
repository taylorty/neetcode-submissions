class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        target = sums // 2

        if sums % 2 != 0:
            return False
        
        def dfs(nums, currSum, i):
            if currSum < 0:
                return False
            if currSum == 0:
                return True
            res = False
            for index in range(i, len(nums)):
                res = res or dfs(nums, currSum - nums[index], index + 1)
                res = res or dfs(nums, currSum, index + 1)
            return res
        
        return dfs(nums, target, 0)
