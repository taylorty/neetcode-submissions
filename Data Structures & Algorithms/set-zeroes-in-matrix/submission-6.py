class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rowZero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        rowZero = True
                    else:
                        matrix[i][0] = 0

        # Zero out inner cells based on markers
        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Handle first column
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        # Handle first row
        if rowZero:
            for c in range(n):
                matrix[0][c] = 0                

        # for i in range(1, m):
        #     if matrix[i][0] == 0:
        #         for j in range(1, n):
        #             matrix[i][j] = 0

        # for j in range(1, n):
        #     if matrix[0][j] == 0:
        #         for i in range(1, m):
        #             matrix[i][j] = 0
        
        # if matrix[0][0] == 0:
        #     for j in range(n):
        #         matrix[0][j] = 0
    
        # if rowZero == True:
        #     for i in range(m):
        #         matrix[i][0] = 0