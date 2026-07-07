class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = [0 for i in range(n + 1)]
        self.memo[0] = 1
        self.memo[1] = 1
        for i in range(2, n + 1):
            self.memo[i] = self.memo[i - 1] + self.memo[i - 2]
        return self.memo[n]