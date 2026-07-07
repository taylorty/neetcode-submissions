class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = max(count, self.dfs(grid, i, j))
        return count
    
    def dfs(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        result = 1
        result += self.dfs(grid, i + 1, j)
        result += self.dfs(grid, i - 1, j)
        result += self.dfs(grid, i, j + 1)
        result += self.dfs(grid, i, j - 1)
        return result