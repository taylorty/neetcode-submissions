class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    count += 1
        minute = 0
        while q:
            size = len(q)
            
            if count == 0:
                return minute
            minute += 1
            for _ in range(size):
                x, y = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    i = x + dr
                    j = y + dc
                    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 1:
                        continue

                    grid[i][j] = 2
                    count -= 1
                    q.append((i, j))
        if count == 0:
            return 0
        return -1

