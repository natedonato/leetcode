class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return nums

        pre_l = [0, nums[0]]

        for i in range(1, len(nums)):
            pre_l.append(max(pre_l[-1], nums[i]))


        pre_r = [nums[-1]]
        for i in reversed(range(1,len(nums))):
            pre_r.append(max(pre_r[-1],nums[i]))
        pre_r.reverse()

        out = []
        out.append(nums[0])

        for i in range(1, len(nums)-1):
            v = nums[i]
            if v > pre_l[i] or v > pre_r[i]:
                out.append(v)

        out.append(nums[-1])

        return out
