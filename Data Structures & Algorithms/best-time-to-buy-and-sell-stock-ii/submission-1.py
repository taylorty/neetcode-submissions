class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        res = 0
        i = 1
        while i < len(prices):
            if prices[i] >= prev:
                res += prices[i] - prev
            prev = prices[i]
            i += 1
        return res