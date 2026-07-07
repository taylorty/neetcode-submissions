class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        i = 0
        j = 0
        count = Counter(s1)
        count2 = Counter()
        for i, ch in enumerate(s2):
            count2[s2[i]] += 1
            if i < n1 - 1:
                continue
            if count2 == count:
                return True
            count2[s2[i - n1 + 1]] -= 1
        return False