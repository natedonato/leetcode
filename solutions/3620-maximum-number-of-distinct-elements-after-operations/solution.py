class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        count = 0
        min_possible_distinct = -math.inf
        nums.sort()

        for n in nums:
            min_possible_distinct = max(min_possible_distinct, n - k)
            if min_possible_distinct <= n + k:
                count += 1
                min_possible_distinct += 1

        return count

