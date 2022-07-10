class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i = len(cost) - 1
        dp = [0] * len(cost)
        minCost = 0
        while i >= 0:
            if i + 2 < len(cost):
                dp[i] = min(cost[i] + dp[i + 1], cost[i] + dp[i + 2])
            else:
                dp[i] = cost[i]
            i-=1
        
        return min(dp[0], dp[1])