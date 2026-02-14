class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_row = [poured]
        for i in range(1,query_row + 1):

            next_row = [0] * (len(prev_row) + 1)
            for i, amt in enumerate(prev_row):
                amt = amt - 1
                if amt > 0:
                    next_row[i] += amt / 2
                    next_row[i+1] += amt / 2

            prev_row = next_row

        return min(prev_row[query_glass], 1.0)
