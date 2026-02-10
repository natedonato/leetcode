class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        l = len(nums)
        longest = 0
        for i in range(l):
            odds = set()
            evens = set()
            for j in range(i, l):
                num = nums[j]
                if num % 2 == 0:
                    evens.add(num)
                else:
                    odds.add(num)

                if len(evens) == len(odds):
                    longest = max(longest, j - i + 1)

        return longest
