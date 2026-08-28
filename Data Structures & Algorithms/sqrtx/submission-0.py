class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = x // 2 + 1
        while s < e:
            m = (e - s + 1) // 2 + s
            if m * m == x:
                return m
            elif m * m < x:
                s = m
            else:
                e = m - 1
        return s