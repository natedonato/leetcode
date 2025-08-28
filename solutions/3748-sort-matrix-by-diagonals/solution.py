class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        for i in range(0, len(grid)):
            diagonal = []
            point = [i,0]
            
            for _ in range(len(grid)-i):
                diagonal.append(grid[point[0]][point[1]])
                point[0] += 1
                point[1] += 1
            diagonal.sort()
            point = [i,0]

            for _ in range(len(grid)-i):
                grid[point[0]][point[1]] = diagonal.pop()
                point[0] += 1
                point[1] += 1

        for i in range(1, len(grid[0])):
            diagonal = []
            point = [0,i]
            for _ in range(len(grid) - i):
                diagonal.append(grid[point[0]][point[1]])
                point[0] += 1
                point[1] += 1
            diagonal.sort(reverse=True)
            point = [0,i]
            for _ in range(len(grid)-i):
                grid[point[0]][point[1]] = diagonal.pop()
                point[0] += 1
                point[1] += 1

        return grid

