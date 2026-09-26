class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for i in range(len(nums))]
        
        # Returns the maximum profit from robbing houses considering position n in the array first
        def findMax(n):
            # If we have reached the last house already, return 0
            if n >= len(nums):
                return 0
            elif dp[n] != -1: # If we already calculated the max profits for this index, return that
                return dp[n]

            # Either we can skip this house and rob the next one, or we can rob this one and the house two places down
            maxMoney = max(nums[n] + findMax(n + 2), findMax(n + 1))
            dp[n] = maxMoney
            return maxMoney

        return findMax(0)

            