class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        first = colors[0]
        last = colors[-1]

        max_dist = 0

        for i, c in enumerate(colors):
            if c != first:
                max_dist = max(max_dist, i)
            if c != last:
                max_dist = max(max_dist, len(colors) - i - 1)
        
        return max_dist
