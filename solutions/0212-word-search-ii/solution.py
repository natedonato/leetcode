class trieNode:
    def __init__(self, char, parent = None, endword = None):
        self.char = char
        self.endword = endword
        self.parent = parent
        self.children = {}

    # def __repr__(self):
    #     return str({'char': self.char, "endword":self.endword, 'children':self.children})

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = trieNode("")
        self.board = board

        for word in words:
            node = self.root
            for i in range(len(word)):
                char = word[i]
                if char in node.children:
                    next_node = node.children[char]
                else:
                    next_node = trieNode(char, node)
                node.children[char] = next_node
                node = next_node
            
            node.endword = word
        
        self.output = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(i, j, self.root, set())

        return list(self.output)
    
    def search(self, r, c, trienode, visited):
        
        char = self.board[r][c]
        if char in trienode.children:
            trienode = trienode.children[char]
            
            if trienode.endword is not None:
                self.output.add(trienode.endword)

            if trienode.children:
                visited.add((r,c))
                for n in self.getNeighbors(r,c):
                    if n not in visited:
                        self.search(n[0],n[1],trienode,visited)
                visited.remove((r,c))

    def getNeighbors(self, r, c):
        vects = [[0,1],[0,-1],[1,0],[-1,0]]
        out = []
        for vect in vects:
            r1 = r + vect[0]
            c1 = c + vect[1]

            if 0 <= r1 and r1 < len(self.board) and 0 <= c1 and c1 < len(self.board[0]):
                out.append((r1,c1))

        return out
