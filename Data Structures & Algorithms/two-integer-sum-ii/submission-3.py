class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1

        while left_index < right_index:
            if numbers[left_index] + numbers[right_index] == target:
                return [left_index + 1, right_index + 1]
            elif numbers[left_index] + numbers[right_index] < target:
                left_index += 1
            else:
                right_index -= 1

        return []