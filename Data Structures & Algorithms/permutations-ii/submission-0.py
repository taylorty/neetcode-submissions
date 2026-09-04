class Solution:
    # 0, 1
    # 1, 2
    # 0, 2
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # result = []
        res = set()
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def dfs(i):
            if i >= len(nums):
                res.add(tuple(nums.copy()))
                return
            
            for j in range(i, len(nums)):
                # if j > 0 and nums[j] == nums[j - 1]:
                #     continue
                swap(nums, i, j)
                dfs(i + 1)
                swap(nums, j, i)

        dfs(0)
        return list(res)