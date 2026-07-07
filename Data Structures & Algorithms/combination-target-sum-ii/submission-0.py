class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        self.dfs(nums, res, [], 0, set(), 0, target)
        return res
    
    def dfs(self, nums, res, curr, index, visited, s, target):
        if s == target:
            res.append(curr.copy())
            return
        if s > target:
            return
        # res.append(curr.copy())
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            
            curr.append(nums[i])
            self.dfs(nums, res, curr, i + 1, visited, s + nums[i], target)
            curr.pop()
            # visited.remove(nums[i])