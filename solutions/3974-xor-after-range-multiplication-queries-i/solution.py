class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for q in queries:
            l, r, k, v = q
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % 1_000_000_007
                idx += k
        
        out = nums[0]
        for i in range(1, len(nums)):
            out ^= nums[i]

        return out
        
