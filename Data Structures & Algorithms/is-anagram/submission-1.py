class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)
        for k in c1:
            if k not in c2 or c2[k] != c1[k]:
                return False
        return len(c1) == len(c2)