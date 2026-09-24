class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for i in range(len(cost) + 1)]

        # Returns the min cost to climb the stairs starting at stair n
        def minCost(n) -> int:
            if n == len(cost):
                return 0
            if n == len(cost) - 1:
                return cost[-1]
            
            if dp[n] != -1:
                return dp[n]

            dp[n] = min(cost[n] + minCost(n + 1), cost[n] + minCost(n + 2))
            return dp[n]

        return min(minCost(0), minCost(1))