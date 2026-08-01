class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueIndices = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if (difference in valueIndices.keys()):
                return [valueIndices[difference], i]
            else:
                valueIndices[nums[i]] = i
        return None