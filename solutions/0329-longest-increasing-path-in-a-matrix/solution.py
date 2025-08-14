class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.dp = [ [None] * len(matrix[0]) for j in range(len(matrix)) ]    
        self.matrix = matrix
        self.output = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.solve(i,j)

        return self.output

    def solve(self, r, c):
        if self.dp[r][c] is not None:
            return self.dp[r][c]

        path_length = 1
        current_val = self.matrix[r][c]

        neighbors = self.getValidNeighbors(r,c,current_val)
        best_neighbor = 0
        for neighbor in neighbors:
            best_neighbor = max(best_neighbor, self.solve(neighbor[0],neighbor[1]))
        solution = path_length + best_neighbor
        self.dp[r][c] = solution
        self.output = max(self.output, solution)
        return solution

    def getValidNeighbors(self, r,c,val):
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        neighbors = []

        for vect in dirs:
            dr = vect[0]
            dc = vect[1]

            if r + dr >= 0 and r + dr < len(self.matrix) and c + dc >= 0 and c+dc < len(self.matrix[0]):
                if self.matrix[r+dr][c+dc] > val:
                    neighbors.append([r+dr, c+dc])
        
        return neighbors
