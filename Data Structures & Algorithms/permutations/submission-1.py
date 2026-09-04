class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def dfs(i):
            if i >= len(nums):
                result.append(nums.copy())
                return
            
            for j in range(i, len(nums)):
                swap(nums, i, j)
                dfs(i + 1)
                swap(nums, j, i)

        dfs(0)
        return result