class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        l = len(nums)
        max_to_right = [0] * l
        max_to_right[-1] = nums[-1]

        for i in reversed(range(l-1)):
            max_to_right[i] = max(max_to_right[i+1], nums[i+1])

        max_to_left = nums[0]
        output = 0

        for i in range(1, l-1):
            mid = nums[i]
            max_to_left = max(max_to_left, nums[i-1])
            right = max_to_right[i]
            output = max((max_to_left - mid) * right, output)

        return output
              

