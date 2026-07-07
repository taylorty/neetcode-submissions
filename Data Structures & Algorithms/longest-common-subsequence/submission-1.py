class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #    c a t
        # c  1 1 1
        # r  1 1 1
        # a. 1 2 2
        # b. 1 2 2
        # t. 1 2 3
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[i][j]