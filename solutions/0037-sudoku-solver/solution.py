class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rows = {}
        self.cols = {}
        self.boxes = {}
        for i in range(0,9):
            self.rows[i] = set()
            self.cols[i] = set()
        
        for i in range(0,3):
            self.boxes[i] = {}
            for j in range(0,3):
                self.boxes[i][j] = set()

        for r in range(0,9):
            for c in range(0,9):
                char = board[r][c]
                if(char != "."):
                    self.rows[r].add(char)
                    self.cols[c].add(char)
                    self.boxes[r // 3][c // 3].add(char)

        print(self.btrack(board, 0))

    def btrack(self, board, idx):
        row = idx // 9
        col = idx % 9
        row_square = row // 3
        col_square = col // 3

        if row == 9:
            return True

        if board[row][col] != ".":
            return self.btrack(board, idx + 1)

        for i in range(1,10):
            char = str(i)
            if self.check(board, idx, char):
                board[row][col] = char
                if self.btrack(board, idx + 1):
                    return True
                else:
                    self.rows[row].remove(char)
                    self.cols[col].remove(char)
                    self.boxes[row_square][col_square].remove(char)

        board[row][col] = "."
        return False

    def check(self, board, idx, char):
        row = idx // 9
        col = idx % 9
        row_square = row // 3
        col_square = col // 3

        if char in self.rows[row] or char in self.cols[col] or char in self.boxes[row_square][col_square]:
            return False
        else:
            self.rows[row].add(char)
            self.cols[col].add(char)
            self.boxes[row_square][col_square].add(char)
            return True

