class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_el = math.inf
        max_el = -math.inf
        min_count = 0
        max_count = 0

        for e in nums:
            if e > max_el:
                max_el = e
                max_count = 1
            elif e == max_el:
                max_count += 1

            if e < min_el:
                min_el = e
                min_count = 1
            elif e == min_el:
                min_count += 1

        if min_el == max_el:
            return 0

        return len(nums) - min_count - max_count

