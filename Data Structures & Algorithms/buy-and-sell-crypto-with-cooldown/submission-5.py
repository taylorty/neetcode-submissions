class Solution:
    # buy hold sell
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (index, canBuy)
        def dfs(index, canBuy):
            if index >= len(prices):
                return 0
            if (index, canBuy) in dp:
                return dp[(index, canBuy)]

            if canBuy:
                # Option 1: Buy today (subtract price, move to next day, cannot buy)
                buy = -prices[index] + dfs(index + 1, False)
                # Option 2: Skip today (move to next day, can still buy)
                skip = dfs(index + 1, True)
                dp[(index, canBuy)] = max(buy, skip)
            else:
                # Option 1: Sell today (add price, move TWO days forward for cooldown, can buy)
                sell = prices[index] + dfs(index + 2, True)
                # Option 2: Hold the stock (move to next day, still cannot buy)
                skip = dfs(index + 1, False)
                dp[(index, canBuy)] = max(sell, skip)
            return dp[(index, canBuy)]
        return dfs(0, True)