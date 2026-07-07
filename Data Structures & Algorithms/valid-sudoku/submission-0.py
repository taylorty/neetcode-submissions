class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = [set() for i in range(9)]
        y = [set() for i in range(9)]
        z = [set() for i in range(9)]

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                index = i // 3 * 3 + j // 3
                # 1, 3 -> 1
                # 4, 3 -> 4

                if board[i][j] in x[i] or board[i][j] in y[j] or board[i][j] in z[index]:
                    return False
                x[i].add(board[i][j])
                y[j].add(board[i][j])
                z[index].add(board[i][j])
        return True