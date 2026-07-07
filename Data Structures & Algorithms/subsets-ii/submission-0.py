class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sorted(nums)
        self.dfs(sorted(nums), res, [], 0, set())
        return res
    
    def dfs(self, nums, res, curr, index, visited):
        # if len(curr) == len(nums):
        #     res.append(curr.copy())
        #     return
        res.append(curr.copy())
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            # visited.add(nums[i])
            self.dfs(nums, res, curr, i + 1, visited)
            curr.pop()
            # visited.remove(nums[i])