class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, cols-1

        while l < rows and r >= 0:
            if matrix[l][r] > target:
                r -= 1
            elif matrix[l][r] < target:
                l += 1
            else:
                return True
        return False

