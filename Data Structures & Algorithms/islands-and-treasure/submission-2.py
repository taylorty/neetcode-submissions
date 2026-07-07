class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
        while q:
            x, y = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i = x + dr
                j = y + dc
                if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 2147483647:
                    continue

                grid[i][j] = grid[x][y] + 1
                q.append((i, j))

