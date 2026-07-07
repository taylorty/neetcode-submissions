class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = set()
        i = j = 0
        result = 0
        while j < len(s):
            # While the condition is violated, the window is invalid, so shrink the window by
            # advancing the left pointer.
            while s[j] in m:
                m.remove(s[i])
                i += 1
            # Once the window is valid, process it and then expand the window by advancing the
            # right pointer.
            result = max(result, j - i + 1)
            m.add(s[j])
            j += 1
        return result