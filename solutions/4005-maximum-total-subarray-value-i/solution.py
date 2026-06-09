class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mv = max(nums)
        minv = min(nums)
        return (mv - minv) * k
