class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        for r in range(0, len(matrix)):
            stack = []

            for c in range(0, len(matrix[0])):
                matrix[r][c] = int(matrix[r][c])
                if r > 0 and matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]

                current_height = matrix[r][c]
                current_idx = c
                prev_idx = current_idx
                while stack and stack[-1][0] > current_height:
                    (prev_height, prev_idx) = stack.pop()
                    prev_area = (current_idx - prev_idx) * prev_height
                    max_area = max(prev_area, max_area)

                if not stack or stack[-1][0] != current_height:
                    stack.append((current_height, prev_idx))

            while stack:
                    current_idx = len(matrix[0])
                    (prev_height, prev_idx) = stack.pop()
                    prev_area = (current_idx - prev_idx) * prev_height
                    max_area = max(prev_area, max_area)

        return max_area
            
