class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        result = []
        l = 0
        r = n - 1
        u = 0
        d = m - 1
        while l <= r and u <= d:

            # go right
            # print(l, r)
            for k in range(l, r + 1):
                result.append(matrix[u][k])
                print(k)
            u += 1
            

            # go down
            for k in range(u, d + 1):
                result.append(matrix[k][r])
            r -= 1

            if not (l <= r and u <= d):
                break
            # go left

            # print ("d", d)
            for k in range(r, l - 1, -1):
                print ("d k m", d, k, matrix[d][k])
                result.append(matrix[d][k])
            d -= 1

            if not (l <= r and u <= d):
                break
            # go up
            for k in range(d, u - 1, -1):
                result.append(matrix[k][l])
            l += 1

        return result