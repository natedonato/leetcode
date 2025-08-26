class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = 0
        sum_sq = 0
        for d in dimensions:
            sum_sq_current = (d[0] ** 2) + (d[1] ** 2)
            if sum_sq_current > sum_sq:
                sum_sq = sum_sq_current
                area = d[0] * d[1]
            elif sum_sq_current == sum_sq:
                area = max(area, d[0] * d[1])

        return area
