class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            if not stack:
                stack.append((h, i))
                continue
            prev_idx = i
            while stack and stack[-1][0] >= h:
                prev_height, prev_idx = stack.pop()
                max_area = max(max_area, prev_height * (i - prev_idx))

            stack.append((h, prev_idx))

        while stack:
            prev_height, prev_idx = stack.pop()
            max_area = max(max_area, prev_height * (len(heights) - prev_idx))

        return max_area


