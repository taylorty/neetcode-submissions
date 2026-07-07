class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minfornow = float('inf')
        # maxfornow = float('-inf')
        result = 0
        for price in prices:
            if price < minfornow:
                minfornow = price
            result = max(result, price - minfornow)
        return result