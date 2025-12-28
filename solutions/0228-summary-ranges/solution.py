class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ranges = []
        range_start = nums[0]
        prev = nums[0]
        for num in nums[1:]:
            if num == prev + 1:
                prev = num
            else:
                if range_start == prev:
                    ranges.append(str(prev))
                else:
                    ranges.append(str(range_start) + "->" + str(prev))

                range_start = num
                prev = num

        if range_start == prev:
            ranges.append(str(prev))
        else:
            ranges.append(str(range_start) + "->" + str(prev))

        return ranges
