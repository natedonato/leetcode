class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        out = map(lambda num: 0 if num % 2 == 0 else 1, nums)
        return sorted(list(out))
        
