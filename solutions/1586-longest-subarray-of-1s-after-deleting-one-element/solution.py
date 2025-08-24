class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev_count = 0
        prev_end_idx = -math.inf
        connect_possible = False
        current_count = 0
        longest = 0

        for i in range(len(nums)):
            
            if nums[i] == 1:
                if current_count == 0:
                    if prev_end_idx == i - 2:
                        connect_possible = True
                    else:
                        connect_possible = False
                
                current_count += 1
                if connect_possible:
                    longest = max(longest, current_count + prev_count)
                else:
                    longest = max(longest, current_count)

            else:
                if current_count != 0:
                    prev_count = current_count
                    prev_end_idx = i-1
                    current_count = 0

        if longest == len(nums):
            return longest - 1
        
        return longest
