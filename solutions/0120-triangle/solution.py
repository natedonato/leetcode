class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for r in range(m):
            if(r > 0):
                triangle[r][0] += triangle[r-1][0]
                triangle[r][r] += triangle[r-1][r-1]

                for i in range(1,r):
                    triangle[r][i] += min(triangle[r-1][i-1], triangle[r-1][i])

        return min(triangle[m-1])
