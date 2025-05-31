class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        queue = deque()
        queue.append(1)
        n = len(board)
        target = n ** 2
        moves = 0
        visited = set()
        visited.add(1)

        while(queue):
            l = len(queue)
            for i in range(0,l):
                current = queue.popleft()
                if(current == target):
                    return moves
                
                for i in range(6):
                    next_square = current + i + 1 
                    if(next_square > target):
                        continue
                         
                    coord = self.numToCoord(next_square, n)
                    value = board[coord[0]][coord[1]]

                    next_square = current + i + 1 
                    if(next_square > target):
                        continue

                    coord = self.numToCoord(next_square, n)
                    value = board[coord[0]][coord[1]]

                    if value != -1:
                        next_square = value
                            
                    if(next_square in visited):
                        continue
                    else:
                        visited.add(next_square)
                        queue.append(next_square)

            moves += 1

        return -1
    

    def numToCoord(self, num, n):
        num -= 1
        row = (num // n)
        col = num % n
        polarity = 1 if row % 2 == 0 else -1

        if polarity == 1:
            final_col = col
        else:
            final_col = n - col - 1 

        final_row = n - row - 1
        
        return (final_row, final_col)
      
