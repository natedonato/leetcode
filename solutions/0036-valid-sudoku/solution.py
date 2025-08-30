class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(9):
            s = set()
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    if val in s:
                        return False
                    s.add(val)

        for c in range(9):
            s = set()
            for r in range(9):
                val = board[r][c]
                if val != ".":
                    if val in s:
                        return False
                    s.add(val) 

        for r1 in range(3):
            r1 *= 3
            for c1 in range(3):
                c1 *= 3
                s = set()
                for dr in range(3):
                    for dc in range(3):
                        val = board[r1 + dr][c1 + dc]
                        if val != ".":
                            if val in s:
                                return False
                            s.add(val)

        return True
