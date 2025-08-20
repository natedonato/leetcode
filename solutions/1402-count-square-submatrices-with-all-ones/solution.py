class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        count = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] != 0:
                    if c == 0 or r == 0:
                        prev = [0]
                    else:
                        prev = [matrix[r-1][c],matrix[r-1][c-1],matrix[r][c-1]]
                    current = min(prev) + 1
                    count += current
                    matrix[r][c] = current
                    
        return count

