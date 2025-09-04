class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        self.grid = coins
        self.m = len(coins)
        self.n = len(coins[0])
        self.cache = {}
        return self.solveDp(0, 0, 0)

    def solveDp(self, r, c, skip_count=0):
        if (r, c, skip_count) in self.cache:
            return self.cache[(r, c, skip_count)]

        current_val = self.grid[r][c]
        possible_solutions = []
        isFinalSquare = False

        if r == self.m - 1 and c == self.n - 1:
            isFinalSquare = True

        # skip case
        if current_val < 0 and skip_count < 2:
            if isFinalSquare:
                possible_solutions.append(0)
            else:
                if r < self.m-1:
                    possible_solutions.append(self.solveDp(r+1,c,skip_count + 1))
                if c < self.n-1:
                    possible_solutions.append(self.solveDp(r,c+1,skip_count + 1))

        # no robber or no skips case
        if isFinalSquare:
            possible_solutions.append(current_val)
        else:
            if r < self.m-1:
                possible_solutions.append(current_val + self.solveDp(r+1,c,skip_count))
            if c < self.n-1:
                possible_solutions.append(current_val + self.solveDp(r,c+1,skip_count))

        final = max(possible_solutions)
        self.cache[(r,c,skip_count)] = final

        return final


        
