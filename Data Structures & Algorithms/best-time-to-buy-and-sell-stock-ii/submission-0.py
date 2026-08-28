class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        res = 0
        i = 0
        while i < len(prices):
            if i > 0:
                if prices[i] < prev:
                    prev = prices[i]
                else:
                    res += prices[i] - prev
                    prev = prices[i]
            i += 1
        return res