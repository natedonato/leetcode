class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        current = nums[0]
        isIncreasing = None

        for i in range(1, len(nums)-1):
            next_item = nums[i]
            
            if next_item < nums[i-1]:
                isIncreasing = False
            
            if next_item > nums[i-1]:
                isIncreasing = True
            
            if next_item > nums[i + 1]:
                if isIncreasing == True:
                    count += 1

            if next_item < nums[i + 1]:
                if isIncreasing == False:
                    count += 1

        return count
