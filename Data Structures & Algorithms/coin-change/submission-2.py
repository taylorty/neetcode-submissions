class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [1000 for i in range(amount + 1)]
        # for coin in coins:
            
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
            for i in range(amount + 1):
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        print(dp)
        if dp[amount] == 1000:
            return -1
        return dp[amount] 