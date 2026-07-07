class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(res, n, k, 0, [])
        return res
        
        
    def dfs(self, res, n, k, index, curr):
        if len(curr) == k:
            res.append(curr.copy())
            return
        
        for i in range(index, n):
            curr.append(i + 1)
            self.dfs(res, n, k, i + 1, curr)
            curr.pop()