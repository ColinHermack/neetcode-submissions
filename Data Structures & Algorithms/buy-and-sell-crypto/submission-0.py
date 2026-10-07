class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        start = 0
        end = 1
        maxProfit = 0
            
        while end < len(prices):
            if prices[start] > prices[end]:
                start = end
            if prices[end] - prices[start] > maxProfit:
                maxProfit = prices[end] - prices[start]
            end += 1

        return maxProfit