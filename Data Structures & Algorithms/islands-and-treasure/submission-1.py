class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        while q:
            x, y, path = q.popleft()
            # if grid[x][y] == float('inf'):
            #     grid[x][y] = path
            #     return
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i = x + dr
                j = y + dc
                if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != 2147483647:
                    continue
                # if str(i) + " " + str(j) in visited:
                #     continue
                # visited.add(str(i) + " " + str(j))
                grid[i][j] = grid[x][y] + 1
                q.append((i, j, path + 1))

