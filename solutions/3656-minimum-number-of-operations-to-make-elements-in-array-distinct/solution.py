class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        for i in range(n-1, -1,-1):
            num = nums[i]
            if num in seen:
                return math.ceil((i + 1) / 3)
            else:
                seen.add(num) 

        return 0
