class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        unique = set()
        nums.sort()
        n = len(nums)
        
        for i in range(0, n-3):
            fixed_1 = nums[i]
            for j in range(i+1, n-2):
                fixed_2 = nums[j]
                left = j+1
                right = n-1

                while(left < right):
                    current_sum = fixed_1 + fixed_2 + nums[left] + nums[right]
                    if current_sum == target:
                        quadruplet = [fixed_1, fixed_2, nums[left], nums[right]]
                        key = ",".join(str(el) for el in quadruplet)
                        if key not in unique:
                            output.append(quadruplet)
                            unique.add(key)

                    if current_sum <= target:
                        left += 1
                    else:
                        right -= 1
            
        return output

