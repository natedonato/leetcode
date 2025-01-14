class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            current_min_height = min(height[left], height[right])
            current_area = current_min_height * (right - left)
            area = max(area, current_area)

            
            while left < len(height) and height[left] <= current_min_height:
                left += 1
            while right > 0 and height[right] <= current_min_height:
                right -= 1

        return area
