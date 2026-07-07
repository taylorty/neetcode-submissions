class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = defaultdict(int)
        tMap = Counter(t)
        lengthT = len(t)
        i = j = 0
        have = 0
        need = len(tMap)
        resLen = float('inf')
        result = [-1, -1]
        while j < len(s):
            # While the condition is violated, the window is invalid, so shrink the window by
            # advancing the left pointer.
            m[s[j]] += 1
            if s[j] in tMap and tMap[s[j]] == m[s[j]]:
                have += 1
                
            # while m and m != tMap:
            #     m[s[i]] -= 1
            #     i += 1
            # Once the window is valid, process it and then expand the window by advancing the
            # right pointer.
            while have == need:
                if j - i + 1 < resLen:
                    resLen = j - i + 1
                    result = [i, j]
                m[s[i]] -= 1
                if s[i] in tMap and m[s[i]] < tMap[s[i]]:
                    have -= 1
                i += 1
            j += 1
        if resLen == float('inf'):
            return ""
        i, j = result
        return s[i: j + 1]