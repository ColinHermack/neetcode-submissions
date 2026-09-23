class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) <= 0:
            return False
        elif len(matrix[0]) <= 0:
            return False
        
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target

        if len(matrix) > 1:
            midPoint = int(len(matrix) / 2)
            mid = matrix[midPoint]
            if mid[0] <= target and mid[-1] >= target:
                return self.searchMatrix([mid], target)
            elif mid[0] > target:
                return self.searchMatrix(matrix[:midPoint], target)
            else:
                return self.searchMatrix(matrix[midPoint:], target)
        
        if len(matrix) == 1:
            midPoint = int(len(matrix[0]) / 2)
            if matrix[0][midPoint] == target:
                return True
            elif matrix[0][midPoint] < target:
                matrix[0] = matrix[0][midPoint:]
            else:
                matrix[0] = matrix[0][:midPoint]
            return self.searchMatrix(matrix, target)