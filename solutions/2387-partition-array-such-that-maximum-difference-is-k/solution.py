class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        current = nums[0]
        count = 1

        for i in range(1, len(nums)):
            next_el = nums[i]
            if current + k < next_el:
                count += 1
                current = next_el
            
        return count
