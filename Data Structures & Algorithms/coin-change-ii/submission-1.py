class Solution:
    #    1 2 3 4
    # 1  1 1 1 1
    # 2  0 2 2 3
    # 3  0 0 1 

    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        # How many ways can we form amount a using coins starting from index i
        def dfs(i, curr_amount):
            if curr_amount == 0:
                return 1
            if i >= len(coins):
                return 0
            if memo[i][curr_amount] != -1:
                return memo[i][curr_amount]
            res = 0
            if curr_amount >= coins[i]:
                res = dfs(i + 1, curr_amount)
                res += dfs(i, curr_amount - coins[i])
            memo[i][curr_amount] = res
            return res
        return dfs(0, amount)

        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a]
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]