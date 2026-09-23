class Solution:
    def binary_search(self, nums: List[int], target: int, start: int, end: int) -> int:

        if (end < start):
            return -1

        if end == start and nums[start] == target:
            return start
        elif end == start:
            return -1

        midpoint = int((start + end) / 2)

        if (nums[midpoint] == target):
            return midpoint
        elif (nums[midpoint] < target):
            return self.binary_search(nums, target, midpoint + 1, end)
        else:
            return self.binary_search (nums, target, start, midpoint - 1)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)