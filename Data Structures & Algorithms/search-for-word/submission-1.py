class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word, 0, set()):
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
        
        
    
