class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        seen = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                if num not in seen:
                    count += 1
                    seen.add(num)
        return count
