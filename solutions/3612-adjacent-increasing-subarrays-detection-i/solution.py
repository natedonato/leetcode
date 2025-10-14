class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev = 0
        prev_el = math.inf
        curr = 0

        for n in nums:
            if n > prev_el:
                curr += 1

            else:
                prev = curr
                curr = 1

            if curr == 2*k or curr == k and prev >= k:
                return True

                
            prev_el = n

        return False
            
