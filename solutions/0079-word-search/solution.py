class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.word = word
        self.board = board

        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(r, c, 0, set()) == True:
                    return True

        return False

    def dfs(self, r, c, index, visited = set()):
        # print(r,c,index, visited)
        # print(self.word[0:index + 1])

        if (r,c) in visited:
            # print("RC in visited")
            return False

        if self.board[r][c] != self.word[index]:
            # print("Char doesn't match")
            return False

        index += 1

        if index >= len(self.word):
            # print("Return TRUE")
            return True


        visited.add((r,c))
        neighbors = self.getNeighbors(r,c)

        for n in neighbors:
            if self.dfs(n[0],n[1], index, visited) == True:
                return True
        
        visited.remove((r,c))
        return False
    

    def getNeighbors(self, r,c):
        vects = [[0,1],[0,-1],[1,0],[-1,0]]
        out = []
        for vect in vects:
            r1 = r + vect[0]
            c1 = c + vect[1]

            if 0 <= r1 and r1 < len(self.board) and 0 <= c1 and c1 < len(self.board[0]):
                out.append((r1,c1))

        return out
