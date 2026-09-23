class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        minIndex = 0
        maxIndex = len(numbers) - 1

        while (numbers[minIndex] + numbers[maxIndex] != target):
            if (numbers[minIndex] + numbers[maxIndex] > target):
                maxIndex -= 1
            else:
                minIndex += 1
        
        return [minIndex + 1, maxIndex + 1]