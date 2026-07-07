class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res, 0)
        return res

    def dfs(self, s, curr, res, index):
        if index == len(s):
            res.append(curr.copy())
            return True

        for i in range(index, len(s)):
            if self.isPali(s, index, i):
                curr.append(s[index:i + 1])
                self.dfs(s, curr, res, i + 1)
                curr.remove(s[index:i + 1])
        return False
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True