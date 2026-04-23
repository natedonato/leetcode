class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        prev_sums = {}
        prev_scale = {}
        prev_index = {}

        out = [0] * len(nums)
        # left side scores
        for i, val in enumerate(nums):
            if val not in prev_sums:
                prev_sums[val] = 0
                prev_scale[val] = 1
                prev_index[val] = i
            else:
                dist = i - prev_index[val]
                diff = dist * prev_scale[val]
                prev_sums[val] += diff
                prev_scale[val] += 1
                
            prev_index[val] = i
            out[i] = prev_sums[val]

        # right side scores
        prev_sums = {}
        prev_scale = {}
        prev_index = {}
        for i in reversed(range(len(nums))):
            val = nums[i]

            if val not in prev_sums:
                prev_sums[val] = 0
                prev_scale[val] = 1
                prev_index[val] = i
            else:
                dist = prev_index[val] - i
                diff = dist * prev_scale[val]
                prev_sums[val] += diff
                prev_scale[val] += 1
                
            prev_index[val] = i
            out[i] += prev_sums[val]

        return out
