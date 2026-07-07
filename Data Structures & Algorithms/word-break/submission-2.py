class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False for i in range(length + 1)]

        setS = set(wordDict)
        dp[0] = True

        for i in range(1, length + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in setS:
                    dp[i] = True
                    break
        return dp[length]