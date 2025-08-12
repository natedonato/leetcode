class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = -inf
        nums.sort()
        for i in range(len(nums) - 2):
            fixed = nums[i]
            left = i+1
            right = len(nums) - 1
            while(left < right):
                current_sum = fixed + nums[left] + nums[right]
                if abs(target - closest_sum) > abs(target - current_sum):
                    closest_sum = current_sum

                if current_sum == target:
                    return target
                elif current_sum > target:
                    right -= 1
                else:
                    left += 1
                
        return closest_sum
                

