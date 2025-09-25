class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in reversed(range(0, len(triangle) - 1)):
            for c in range(0, len(triangle[r])):
                triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])

        return triangle[0][0]
