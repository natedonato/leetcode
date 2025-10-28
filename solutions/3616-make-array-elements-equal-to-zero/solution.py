class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        left_pre = [0]
        for n in nums:
            left_pre.append(left_pre[-1] + n)

        right_sum = 0
        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                left_sum = left_pre[i]

                if left_sum == right_sum:
                    count += 2
                elif abs(right_sum - left_sum) == 1:
                    count += 1

            else:
                right_sum += nums[i]

        return count
