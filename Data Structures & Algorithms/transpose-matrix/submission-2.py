class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        # 1 2 3
        # 4 5 6
        # 7 8 9

        # Index
        # 1, 0
        # 2, 0
        # 2, 1
        if ROWS == COLS:
            for r in range(ROWS):
                for c in range(r + 1):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

            return matrix

        res = [[0] * ROWS for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                res[c][r] = matrix[r][c]

        return res
