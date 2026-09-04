class Solution:
    # 0, 1
    # 1, 2
    # 0, 2
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        # res = set()
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def dfs(i):
            if i >= len(nums):
                res.append(nums.copy())
                return
            
            for j in range(i, len(nums)):
                if j > i and nums[i] == nums[j]:
                    continue
                swap(nums, i, j)
                dfs(i + 1)
                # swap(nums, j, i)
            
            for j in range(len(nums) - 1, i, -1):
                nums[j], nums[i] = nums[i], nums[j]
        nums.sort()
        dfs(0)
        return res