class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rowsets = [ set() for _ in range(9)]
        self.colsets = [set() for _ in range(9)]
        self.boxsets = [ [ set() for _ in range(3)] for x in range(3)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    self.add(r, c, val)
        
        self.btrack(0)
        
    def canadd(self, r, c, val):
        if val in self.rowsets[r] or val in self.colsets[c] or val in self.boxsets[r // 3][c // 3]:
            return False
        return True

    def add(self, r, c, val):
        self.rowsets[r].add(val)
        self.colsets[c].add(val)
        self.boxsets[r // 3][c // 3].add(val)
        return
        
    def remove(self, r, c, val):
        self.rowsets[r].remove(val)
        self.colsets[c].remove(val)
        self.boxsets[r // 3][c // 3].remove(val)
        return

    def btrack(self, i):
        if i == 81:
            return True
        r = i // 9
        c = i % 9
        val = self.board[r][c]
        if val != ".":
            return self.btrack(i+1)

        for char in "123456789":
            if self.canadd(r,c, char):
                self.add(r,c, char)
                self.board[r][c] = char
                if self.btrack(i+1):
                    return True
                else:
                    self.remove(r,c,char)

        self.board[r][c] = "."
        return False

        
