class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:
            mid1 = (right + left) // 2 // n
            mid2 = (right + left) // 2 % n
            
            if matrix[mid1][mid2] == target:
                return True
            if matrix[mid1][mid2] < target:
                #left = (right + left) // 2 + 1
                left = mid1 * n + mid2 + 1
            else:
                #right = (right + left) // 2 - 1
                right = mid1 * n + mid2 - 1
        return False