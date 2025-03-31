class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square = 0
        m = len(matrix)
        n = len(matrix[0])
        for r in range(0,m):
            for c in range(0,n):
                matrix[r][c] = int(matrix[r][c])

                if r > 0 and c > 0 and matrix[r][c] == 1:
                    matrix[r][c] = min(matrix[r-1][c-1], matrix[r-1][c],matrix[r][c-1]) + 1
                
                max_square = max(matrix[r][c], max_square)

        print(matrix)

        return max_square ** 2
