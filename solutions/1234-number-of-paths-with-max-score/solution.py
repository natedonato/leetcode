class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        dp = [ [[0, 0] for el in row] for row in board]
        dp[-1][-1] = [0,1]

        l = len(board)

        def update(r, c, prev_r, prev_c):
            prev = dp[prev_r][prev_c]
            curr = dp[r][c]
            val = board[r][c]
            if val == "E" or val == "S":
                val = 0
            else:
                val = int(val)
            if prev[1] == 0:
                return

            if curr[0] == prev[0] + val:
                curr[1] += prev[1]
            elif curr[0] < prev[0] + val:
                curr[0] = prev[0] + val
                curr[1] = prev[1]

            curr[1] %= 1_000_000_000 + 7

        for r in reversed(range(l)):
            for c in reversed(range(l)):
                if board[r][c] == 'X':
                    continue
                if r < l - 1:
                    update(r,c,r+1,c)

                if c < l - 1:
                    update(r,c,r,c+1)
                if c < l - 1 and r < l - 1:
                    update(r,c,r+1,c+1)

        return dp[0][0]
