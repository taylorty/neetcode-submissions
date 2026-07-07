class Solution:
    def floodFill(self, images: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        start_color = images[sr][sc]
        if start_color == color:
            return images
        def dfs(images, i, j):
            if i < 0 or j < 0 or i >= len(images) or j >= len(images[0]) or images[i][j] != start_color:
                return
            images[i][j] = color
            dfs(images, i + 1, j)
            dfs(images, i - 1, j)
            dfs(images, i, j + 1)
            dfs(images, i, j - 1)

        dfs(images, sr, sc)
        return images