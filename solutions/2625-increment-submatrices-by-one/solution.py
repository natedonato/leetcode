class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        prefix = [ [0] * n for _ in range(n)]
        output = [ [0] * n for _ in range(n)]
        

        for query in queries:
            [r1,c1,r2,c2] = query
            prefix[r1][c1] += 1
            if c2 + 1 < n:
                prefix[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                prefix[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:  

                prefix[r2+1][c2+1] += 1

        
        for r in range(n):
            current = 0
            for c in range(n):
                current += prefix[r][c]
                prefix[r][c] = current

        for c in range(n):
            current = 0
            for r in range(n):
                current += prefix[r][c]
                prefix[r][c] = current

        return prefix
        
