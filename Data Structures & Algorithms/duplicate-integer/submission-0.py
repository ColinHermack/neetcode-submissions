class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurences = {}
        for num in nums:
            if num in occurences.keys():
                occurences[num] = occurences[num] + 1
            else:
                occurences[num] = 1

        for value in occurences.values():
            if (value > 1):
                return True

        return False