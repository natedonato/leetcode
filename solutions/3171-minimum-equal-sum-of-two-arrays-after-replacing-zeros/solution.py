class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        left_zeroes = 0
        right_zeroes = 0
        left_sum = 0
        right_sum = 0
        for num in nums1:
            if num == 0:
                left_zeroes += 1
                left_sum += 1
            else:
                left_sum += num
        
        for num in nums2:
            if num == 0:
                right_zeroes += 1
                right_sum += 1
            else:
                right_sum += num

        if left_sum >= right_sum and right_zeroes > 0:
            return left_sum
        
        if right_sum >= left_sum and left_zeroes > 0:
            return right_sum
        
        if left_sum == right_sum:
            return left_sum
        
        return -1
