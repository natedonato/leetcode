class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.dp = [[0 for _ in heights[0]] for _ in heights]
        self.m = len(heights)
        self.n = len(heights[0])
        self.result = []
        for r in range(self.m):
            self.expand(r,0,True)
        for c in range(1, self.n):
            self.expand(0,c, True)

        # print(self.dp)

        for r in range(self.m):
            self.expand(r, self.n - 1, False)
        for c in range(self.n):
            self.expand(self.m - 1, c, False)
        
        # print(self.dp)
    
        return self.result

    def expand(self, r, c, isPacific = True):
        val = self.dp[r][c]
        if isPacific:
            if val == 1:
                return
            else:
                self.dp[r][c] = 1
        
        if not isPacific:
            if val == 1:
                self.result.append([r,c])
                self.dp[r][c] = 3
            else:
                if self.dp[r][c] == 2 or self.dp[r][c] == 3:
                    return
                else:
                    self.dp[r][c] = 2

        ns = self.neighbors(r,c)
        for n in ns:
            self.expand(n[0], n[1], isPacific)
    

    def neighbors(self, r, c):
        out = []
        val = self.heights[r][c]
        vects = [[0,1],[0,-1],[1,0],[-1,0] ]
        for [dx, dy] in vects: 
            r1 = r + dx
            c1 = c + dy

            if r1 >= 0 and c1 >= 0 and r1 < self.m and c1 < self.n:
                if val <= self.heights[r1][c1]:
                    out.append((r1,c1))

        return out

[[2,1],
 [1,2]]

[[1, 1],
 [1, 1]] 
