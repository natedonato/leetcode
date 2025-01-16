class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        out = 0
        
        if len(nums1) % 2 != 0:
            for num in nums2:
                out ^= num
        if len(nums2) % 2 != 0:
            for num in nums1:
                out ^= num
        
        return out
