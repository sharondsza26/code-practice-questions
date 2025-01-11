from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for val in range(coin, amount + 1):
                if val - coin >= 0:
                    dp[val] = min(dp[val], dp[val - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0

coins = [2] 
amount = 3
solution = Solution()
result = solution.coinChange(coins, amount)
print(result) 