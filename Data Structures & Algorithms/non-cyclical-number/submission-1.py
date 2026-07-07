class Solution:
    def isHappy(self, n: int) -> bool:
        def res(n):
            val = 0
            while n != 0:
                val += (n % 10) ** 2
                n //= 10
                # print(val)
            return val
        s = set()
        val = res(n)
        
        # if val == 1:
        #     return True
        while val not in s:
            if val == 1:
                return True
            s.add(val)
            val = res(val)
            # print(val)
        return False