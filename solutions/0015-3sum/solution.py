class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = set()
        output = []
        
        for i in range(0, len(nums) - 2):
            first = nums[i]
            target = 0 - first

            l = i + 1
            r = len(nums) - 1
            while(l < r):
                if nums[l] + nums[r] == target:
                    key = f"{nums[i]},{nums[l]},{nums[r]}"
                    if key not in used:
                        used.add(key)
                        output.append([first, nums[l], nums[r]])
                    while(l < r and nums[l] == nums[l + 1]):
                        l += 1
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
            
        return output

#        Strategy:
#        Fix one index as our "base"
#        Now we have a two-sum problem
#           Use a frequency map / set
#           Dedupe results?
