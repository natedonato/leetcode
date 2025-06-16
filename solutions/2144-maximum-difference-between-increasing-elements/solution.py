class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_seen = nums[0]
        for i in range(1, len(nums)):
            current = nums[i]
            if current > min_seen:
                max_diff = max(max_diff, current - min_seen)
            
            min_seen = min(min_seen, current)

        return max_diff
