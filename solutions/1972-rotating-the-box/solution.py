class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        out = [[ "." for _ in range(m)] for _ in range(n)]
        
        for r in range(m):
            next_idx = n - 1
            
            for c in reversed(range(n)):
                val = boxGrid[r][c] 
                if  val == "#":
                    out[next_idx][m - r - 1] = "#"
                    next_idx -= 1
                elif val == "*":
                    out[c][m-r-1] = "*"
                    next_idx = c - 1



        return out
