class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = 0
        while l < len(strs[0]):
            prefix = strs[0][0:l + 1]
            for s in strs:
                if s[0: l + 1] != prefix:
                    return s[0: l]
            l += 1
        return strs[0][0:l + 1]
