class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            # while i < j and not s[i].isalnum():
            #     i += 1
            # while i < j and not s[j].isalnum():
            #     j -= 1
            # if j < 0 or i >= len(s):
            #     return True
            if s[i].lower() != s[j].lower():
                # We found a mismatch. We can either drop the left char (i) 
                # or drop the right char (j).
                skip_left = s[i + 1:j + 1]
                skip_right = s[i:j]
                
                # The remaining substring MUST be a perfect palindrome.
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            i += 1
            j -= 1
        return True