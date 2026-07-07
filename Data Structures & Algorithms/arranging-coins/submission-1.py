class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        res = 0
        s = 0
        while s <= n:
            # if s >= n:
            #     return res
            s += i
            i += 1
            res += 1
        return res - 1