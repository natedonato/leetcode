class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorts = sorted(nums)

        m = {}

        for i, el in enumerate(sorts):
            if el not in m:
                m[el] = i

        for i in range(len(nums)):
            nums[i] = m[nums[i]]

        return nums
