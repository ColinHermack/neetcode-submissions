class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        
        maxWater = end * min(heights[start], heights[end])

        while start < end:
            if (end - start) * min(heights[start], heights[end]) > maxWater:
                maxWater = (end - start) * min(heights[start], heights[end])
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return maxWater