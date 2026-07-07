class Solution:
    # buy hold sell
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (index, canBuy)
        def dfs(prices, i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            res = 0
            if canBuy:
                res += max(-prices[i] + dfs(prices, i + 1, False), dfs(prices, i + 1, True))
            else:
                res += max(prices[i] + dfs(prices, i + 2, True), dfs(prices, i + 1, False))
            dp[(i, canBuy)] = res
            return res
        return dfs(prices, 0, True)