class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(i, j, index, visited):
            if index == len(word):
                return True
            
            if (i < 0 or j < 0 or i >= m or j >= n or 
                word[index] != board[i][j] or (i, j) in visited):
                return False
            
            visited.add((i, j))
            
            # Explore all 4 directions
            res = (dfs(i + 1, j, index + 1, visited) or
                   dfs(i - 1, j, index + 1, visited) or
                   dfs(i, j + 1, index + 1, visited) or
                   dfs(i, j - 1, index + 1, visited))
            
            # BACKTRACK: remove the cell so it can be reused in other paths
            visited.remove((i, j))
            return res

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True

        return False

    def dfs(self, board, i, j, word, index, visited):
        m = len(board)
        n = len(board[0])
        if index == len(word):
            return True
        if i < 0 or j < 0 or j >= n or i >= m or word[index] != board[i][j] or ((i, j)) in visited:
            return False
        visited.add((i, j))
        res = (self.dfs(board, i + 1, j, word, index + 1, visited) or
                self.dfs(board, i - 1, j, word, index + 1, visited) or
                self.dfs(board, i, j + 1, word, index + 1, visited) or
                self.dfs(board, i, j - 1, word, index + 1, visited))
        
        # BACKTRACK: remove the cell so it can be reused in other paths
        visited.remove((i, j))
        return res
        
        
    
