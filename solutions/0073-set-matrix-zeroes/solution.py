class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_cols = set()
        zero_rows = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_cols.add(i)
                    zero_rows.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_cols or j in zero_rows:
                    matrix[i][j] = 0
