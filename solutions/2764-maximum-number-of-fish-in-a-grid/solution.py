class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        best = 0
        
        
        
        def validNeighbors(x, y):
            neighbors = []
            
            vects = [
                [0,1],
                [0, -1],
                [1,0],
                [-1,0]

                ]
            
            for vect in vects:
                x1 = x + vect[0]
                y1 = y + vect[1]
                
                if x1 >= 0 and y1 >= 0 and x1 < m and y1 < n:
                    neighbors.append((x1, y1))
            
            return neighbors
        
        
        def bfs(x,y):
            score = 0
            queue = deque()
            queue.append([x,y])
            
            while queue:
                current = queue.popleft()
                x = current[0]
                y = current[1]
                
                val = grid[x][y]
                
                if val == 0 or (x,y) in visited:
                    continue
                else:
                    visited.add((x,y))
                


                    
                score += val
                
                for n in validNeighbors(x,y):
                    queue.append(n)
                    
            return score
 
        for i in range(0,m):
            for j in range (0,n):
                if (i,j) not in visited:
                    s = bfs(i,j)
                    best = max(best, s)
                    
        
        return best
    
        
