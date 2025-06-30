class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        best = 0

        for num, count in counts.items():
            if num - 1 in counts:
                current = counts[num - 1] + count
                best = max(best, current)

        return best

