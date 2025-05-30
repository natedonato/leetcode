class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        best = 0
        
        while l < r:
            current = (r - l) * min(height[l], height[r])
            best = max(current,best)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
    
        return best
