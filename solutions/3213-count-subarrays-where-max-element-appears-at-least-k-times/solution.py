class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_el = -1
        for num in nums:
            max_el = max(num, max_el)
        
        total = 0
        left = 0
        right = -1
        current_count = 0

        while(left < len(nums)):

            while current_count < k:
                right += 1
                if right >= len(nums):
                    return total
                if nums[right] == max_el:
                    current_count += 1
                    
            total += len(nums) - right
            if nums[left] == max_el:
                current_count -= 1
            left += 1

        return total 

