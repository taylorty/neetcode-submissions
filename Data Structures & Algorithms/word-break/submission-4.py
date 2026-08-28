class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 0 1 2 3 4 5 6 7
        # n e e t c o d e
        # F F F T F F F T
        length = len(s)
        dp = [False for i in range(length)]
        # dp[0] = True
        wordSet = set(wordDict)
        for i in range(length + 1):
            for j in range(i):
                if j == 0 and s[j:i] in wordSet:
                    dp[i - 1] = True
                    break
                # print(s[j:i], dp[j])
                if s[j:i] in wordSet and dp[j - 1]:
                    dp[i - 1] = True
                    break
        # print(dp)
        return dp[length - 1]