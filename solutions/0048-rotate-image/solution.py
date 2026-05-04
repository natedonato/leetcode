class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.m = len(matrix)
        self.n = len(matrix[0])

        for r in range(self.m):
            for c in range(r):
                r1, c1 = self.invert((r,c))
                matrix[r][c],matrix[r1][c1] = matrix[r1][c1], matrix[r][c]

        for r in range(self.m):
            for c in range(self.n // 2):
                r1, c1 = self.flipH((r,c))
                matrix[r][c],matrix[r1][c1] = matrix[r1][c1], matrix[r][c]


    def invert(self, point):
        r, c = point
        return (c,r)
    
    def flipH(self, point):
        r, c = point
        return(r, self.n - c - 1)
