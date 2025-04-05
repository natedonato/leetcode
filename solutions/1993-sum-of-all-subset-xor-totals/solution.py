class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0

        
        def btrack(i, current_xor_total):
            if( i >= n):
                return 0
        
            nonlocal total_sum
            
            next_num = nums[i]

            # skip number
            btrack(i+1, current_xor_total)
            # take number
            current_xor_total ^= next_num
            btrack(i+1, current_xor_total)

            total_sum += current_xor_total
            return 0
        
        btrack(0, 0)

        return total_sum


