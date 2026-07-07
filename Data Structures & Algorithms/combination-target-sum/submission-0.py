class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
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
            # if nums[i] in visited:
            #     continue
            curr.append(nums[i])
            # visited.add(nums[i])
            self.dfs(nums, res, curr, i, visited, s + nums[i], target)
            curr.pop()
            # visited.remove(nums[i])