class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_dist = math.inf
        coords = {}

        for i, n in enumerate(nums):
            if n not in coords:
                coords[n] = []

            coords[n].append(i)

            if len(coords[n]) > 2:
                min_dist = min(min_dist, 2*(i - coords[n][-3]))


        if min_dist == math.inf:
            return -1
        
        return min_dist



