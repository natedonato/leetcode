class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])

        for r in range(len(rows)):
            for c in range(len(cols)):
                if mat[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1

        count = 0
        for r in range(len(rows)):
            for c in range(len(cols)):
                if mat[r][c] == 1:
                    if rows[r] == 1 and cols[c] == 1:
                        count += 1

        return count

