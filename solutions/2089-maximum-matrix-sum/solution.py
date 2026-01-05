class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg_count = 0
        min_val = math.inf

        for r in matrix:
            for e in r:
                val = abs(e)
                total += val
                min_val = min(min_val, val)
                if e < 0:
                    neg_count += 1

        if neg_count % 2 == 0:
            return total
        return total - (2*min_val)
