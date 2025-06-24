class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        out = []
        prev_last_idx = 0

        for index, el in enumerate(nums):
            if el == key:
                for i in range(max(prev_last_idx, index - k), min(index + k + 1, len(nums))):
                    out.append(i)
                prev_last_idx = index + k + 1

        return out
