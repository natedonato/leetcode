class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        current_row = 1
        out = []

        while(current_row <= numRows):
            row = [1] * current_row
            if(current_row > 2):
                prev_row = out[-1]
                for i in range(1, current_row - 1):
                    row[i] = prev_row[i - 1] + prev_row[i]
            
            out.append(row)
            current_row += 1

        return out
