class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)

        while(left < right):
            mid = (right - left) // 2 + left
            val = nums[mid]

            if(val >= 0):
                right = mid
            else:
                left = mid + 1
            
        negative_count = left 
        right = len(nums)
        
        while(left < right):
            mid = (right - left) // 2 + left
            val = nums[mid]
            if(val > 0):
                right = mid
            else:
                left = mid + 1

        pos_count = len(nums) - left
        return max(negative_count, pos_count)

