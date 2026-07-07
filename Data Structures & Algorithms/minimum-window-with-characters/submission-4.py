class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        size = len(count)
        i = j = 0
        curr = 0
        min_len = float('inf')
        min_str = ""
        while i < len(s):
            if s[i] in count:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    size -= 1

            while size == 0:
                if i - j + 1 < min_len:
                    min_len = i - j + 1
                    min_str = s[j:i + 1]
                if s[j] in count:
                    if count[s[j]] == 0:
                        size += 1
                    count[s[j]] += 1
                    
                j += 1
            i += 1

        return min_str

            
