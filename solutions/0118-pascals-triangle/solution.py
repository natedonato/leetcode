class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        while len(out) < numRows:
            next_row = []
            next_row.append(1)
            for i in range(len(out[-1]) - 1):
                next_row.append(out[-1][i] + out[-1][i+1])
            next_row.append(1)
            out.append(next_row)

        return out
