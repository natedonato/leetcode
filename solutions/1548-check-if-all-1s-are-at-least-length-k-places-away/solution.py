class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -k -1
        for i, e in enumerate(nums):
            if e == 1:
                if i - prev <= k:
                    return False
                prev = i

        return True
                    
