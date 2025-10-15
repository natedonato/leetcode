class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev_el = math.inf
        prev = 0
        current = 0
        best = 0

        for n in nums:
            if n > prev_el:
                current += 1
            else:
                prev = current
                current = 1
            prev_el = n
            
            best = max(best, current // 2, min(prev, current))

        return best
