class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        arr = []
        cols = len(encodedText) // rows

        for i in range(rows):
            arr.append(encodedText[i*cols: i * cols + cols + 1])

        pos = [0,0]
        output = ""
        while pos[1] < cols:
            output += arr[pos[0]][pos[1]]
            pos[0] += 1
            pos[1] += 1
            if pos[0] == rows or pos[1] == cols:
                pos[1] -= pos[0] - 1
                pos[0] = 0
            
        return output.rstrip()

