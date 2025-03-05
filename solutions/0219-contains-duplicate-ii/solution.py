class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}

        for idx, val in enumerate(nums):
            if val in indexes and idx - indexes[val] <= k:
                return True
            
            indexes[val] = idx

        return False
