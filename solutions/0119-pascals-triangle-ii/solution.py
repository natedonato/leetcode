class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        while(len(row) < rowIndex + 1):
            prev = 1
            for i in range(1, len(row)):
                temp = row[i]
                row[i] = prev + row[i]
                prev = temp
            row.append(1)

        return row
