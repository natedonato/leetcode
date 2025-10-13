class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False

        l = 0
        r = m
        while l < r:
            mid = (r - l)//2 + l
            val = matrix[mid][0]

            if val > target:
                r = mid
            else:
                l = mid + 1

        row = l - 1

        l = 0
        r = n
        while l < r:
            mid = (r - l)//2 + l
            val = matrix[row][mid]
            if val > target:
                r = mid
            else:
                l = mid + 1

        return matrix[row][l-1] == target

