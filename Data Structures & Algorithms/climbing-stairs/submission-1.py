class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n + 1)]

        # Returns the ways to reach the top when there are n stairs remaining
        def ways(n):
            if n == 0 or n == 1:
                return 1

            if dp[n] != -1:
                return dp[n]

            dp[n] = ways(n - 1) + ways(n - 2)
            return dp[n]

        return ways(n)