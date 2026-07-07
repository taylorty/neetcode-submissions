class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                dp[i][i + l - 1] = (s[i] == s[i + l - 1] and
                                    (i + 1 > (i + l - 2) or
                                    dp[i + 1][i + l - 2]))

        res = []
        self.dfs_dp(dp, s, [], res, 0)
        # self.dfs(s, [], res, 0)
        return res
    
    def dfs_dp(self, dp, s, curr, res, index):
        if index == len(s):
            res.append(curr.copy())
            return
        for i in range(index, len(s)):
            if dp[index][i]:
                curr.append(s[index:i + 1])
                self.dfs_dp(dp, s, curr, res, i + 1)
                curr.pop()

    def dfs(self, s, curr, res, index):
        if index == len(s):
            res.append(curr.copy())
            return True

        for i in range(index, len(s)):
            if self.isPali(s, index, i):
                curr.append(s[index:i + 1])
                self.dfs(s, curr, res, i + 1)
                curr.pop()
        return False
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True