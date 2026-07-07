class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = 0
        self.max_length = 0
        self.result = ""
        for i in range(len(s)):
            self.countPali(s, i, i)
            self.countPali(s, i, i + 1)
        return self.result

    def countPali(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > self.max_length:
                self.result = s[l: r + 1]
                self.max_length = r - l + 1
            l -= 1
            r += 1
