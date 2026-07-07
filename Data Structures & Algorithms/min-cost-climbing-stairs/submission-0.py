class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.memo = [0] * (n + 1)

        self.memo[0] = 0
        self.memo[1] = 0
        for i in range(2, n + 1):
            self.memo[i] = min(self.memo[i - 1] + cost[i - 1], self.memo[i - 2] + cost[i - 2])
        return max(self.memo[n], self.memo[n - 1])