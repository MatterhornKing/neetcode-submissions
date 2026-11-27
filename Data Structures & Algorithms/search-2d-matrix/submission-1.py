class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (right + left) // 2
            i = mid // n
            j = mid % n
            
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                #left = (right + left) // 2 + 1
                #left = mid1 * n + mid2 + 1
                left = mid + 1
            else:
                #right = (right + left) // 2 - 1
                #right = mid1 * n + mid2 - 1
                right = mid - 1
        return False