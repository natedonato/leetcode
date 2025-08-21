class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        count = 0

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if c and mat[r][c]:
                    mat[r][c] += mat[r][c-1]
                current_val = mat[r][c]
                for i in range(r, -1,-1):
                    current_val = min(current_val, mat[i][c])
                    if current_val == 0:
                        break
                    else:
                        count += current_val

        return count
