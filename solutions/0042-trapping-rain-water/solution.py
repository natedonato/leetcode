class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        rain = 0
        max_left = 0
        max_right = 0

        l = 0
        r = len(height) - 1           
        while(l < r):
            left_wall = height[l]
            right_wall = height[r]
            min_height = min(max_left, max_right)

            if(left_wall < min_height):
                rain += min_height - left_wall
            if(right_wall < min_height):
                rain += min_height - right_wall

            max_left = max(max_left, left_wall)
            max_right = max(max_right, right_wall)
            
            if(left_wall <= right_wall):
                l += 1
            else:
                r -= 1
        
        return rain


