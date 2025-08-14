class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        table = [0] * (len(nums)+2)

        for num in nums:
            if num > 0 and num < len(table):
                table[num] = 1

        for i in range(1, len(table)):
            if table[i] != 1:
                return i

