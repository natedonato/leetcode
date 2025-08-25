class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        out = [mat[0][0]]
        m = len(mat)
        n = len(mat[0])

        current = [0,0]
        vect = [-1,1]

        def flipVect():
            vect[0] *= -1
            vect[1] *= -1

        while len(out) < m * n:
            current[0] += vect[0]
            current[1] += vect[1]

            if current[0] == -1 and current[1] == n:
                current[0] += 2
                current[1] -= 1
                flipVect()
            elif current[0] == -1:
                current[0] += 1
                flipVect()
            elif current[1] == -1 and current[0] == m:
                current[1] += 2
                current[0] -= 1
                flipVect()
            elif current[1] == -1:
                current[1] += 1
                flipVect()
            elif current[0] == m:
                current[1] += 2
                current[0] -= 1
                flipVect()
            elif current[1] == n:
                current[0] += 2
                current[1] -= 1
                flipVect()
            
            out.append(mat[current[0]][current[1]])

        return out
