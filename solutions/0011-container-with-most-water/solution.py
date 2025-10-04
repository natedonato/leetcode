class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.height = height
        best = 0
        l = 0
        r = len(height) - 1

        while l < r:
            best = max(best, self.area(l,r))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return best

    def area(self, l, r):
        return min(self.height[l], self.height[r]) * (r - l)
