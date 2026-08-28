class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 0 1 2 3 4 5 6 7
        # n e e t c o d e
        # F F F T F F F T
        n = len(s)
        word_set = set(wordDict)
        max_len = max((len(w) for w in wordDict), default=0)
        
        # dp[i] is True if s[:i] can be segmented
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # Only look back as far as the longest word in wordDict
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Early exit once valid segmentation is found

        return dp[n]