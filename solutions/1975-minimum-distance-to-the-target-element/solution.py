class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = math.inf

        for i, n in enumerate(nums):
            if n == target:
                min_dist = min(min_dist, abs(start - i))

        return min_dist
