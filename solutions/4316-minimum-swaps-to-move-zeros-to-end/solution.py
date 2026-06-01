class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        c = nums.count(0)
        n = nums[-c:].count(0)

        return c - n
