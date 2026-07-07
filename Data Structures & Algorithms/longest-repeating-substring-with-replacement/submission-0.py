class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = defaultdict(int)
        i = j = 0
        result = 0
        while j < len(s):
            # While the condition is violated, the window is invalid, so shrink the window by
            # advancing the left pointer.
            # print(i, j)
            # print("j - i + 1")
            # print(j - i + 1)
            m[s[j]] += 1
            # if m: print(max(m.values()))
            # print("m and j - i + 1 - max(m.values()) > k")
            # print(m and j - i - max(m.values()) > k)
            while m and j - i + 1 - max(m.values()) > k:
                m[s[i]] -= 1
                i += 1
            # Once the window is valid, process it and then expand the window by advancing the
            # right pointer.
            result = max(result, j - i + 1)
            
            j += 1
        return result