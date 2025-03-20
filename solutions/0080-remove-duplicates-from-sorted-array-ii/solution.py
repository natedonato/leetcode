class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_index = 0
        current_index = 0
        
        prev_el = None
        prev_count = 0
        l = len(nums)
        while(current_index < l):
            el = nums[current_index]
            if(el == prev_el):
                prev_count += 1
            else:
                prev_count = 1
                prev_el = el
            
            if prev_count <= 2:
                nums[next_index] = el
                next_index += 1

            current_index += 1

        return next_index
