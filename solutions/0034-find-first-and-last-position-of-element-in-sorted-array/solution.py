class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        # bsearch for start
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            val = nums[mid]
            if(val >= target):
                right = mid
            else:
                left = mid + 1

        ## left is first index of target or where target would be
        if nums[left] != target:
            return [-1,-1]
        else:
            out = [left]

        # bsearch for end
        left = 0
        right = len(nums)

        while left < right:
            mid = (right - left) // 2 + left
            val = nums[mid]
            
            if (val > target):
                right = mid
            else:
                left = mid + 1

        out.append(left - 1)

        return out
        

