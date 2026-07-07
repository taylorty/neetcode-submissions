class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def helper(i, j):
            if i == len(s1) and j == len(s2):
                return True
                
            if (i, j) in dp:
                return dp[(i, j)]

            if i < len(s1) and s1[i] == s3[i + j] and helper(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[i + j] and helper(i, j + 1):
                return True
            # if s3[k] == s1[i] or s3[k] == s2[j]:
            #     return True

            dp[(i, j)] = False
            return False
        return helper(0, 0)
        