class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        middle_sum = 0
        n = len(fruits)
        for i in range(n):
            middle_sum += fruits[i][i]

        prev = [-math.inf] * n
        prev[n-1] = fruits[0][n-1]

        for row in range(1,n-1):
            current_row = [-math.inf] * n
            for i in range(row + 1,n):
                best = prev[i]
                if i - 1 >= 0:
                    best = max(best, prev[i-1])
                if i + 1 < n:
                    best = max(best, prev[i+1])
                current_row[i] = best + fruits[row][i]
            prev = current_row
        
        best_right = prev[-1]

        prev = [-math.inf] * n
        prev[n-1] = fruits[n-1][0]

        for col in range(1,n-1):
            current_row = [-math.inf] * n
            for i in range(col + 1,n):
                best = prev[i]
                if i - 1 >= 0:
                    best = max(best, prev[i-1])
                if i + 1 < n:
                    best = max(best, prev[i+1])
                current_row[i] = best + fruits[i][col]
            prev = current_row

        best_left = prev[-1]
        score = best_right + best_left + middle_sum
        
        return score


