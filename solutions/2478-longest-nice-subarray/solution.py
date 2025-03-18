class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        running_and = 0
        best_length = 0
        l = 0
        length = len(nums)
        for r in range(0, length):
            next_num = nums[r]

            while(running_and & next_num != 0):
                running_and ^= nums[l]
                l += 1
            
            running_and |= next_num
            best_length = max(best_length, r - l + 1)

        return best_length

