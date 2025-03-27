class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        x = -1
        l = len(nums)
        for i in range(0, l):
            num = nums[i]
            counts[num] += 1
            if counts[num] > l // 2:
                x = num

        left_count = 0
        right_count = counts[x]

        for i in range(0,l):
            left_length = i + 1
            right_length = l - i - 1
            if nums[i] == x:
                left_count += 1
                right_count -= 1

            if (left_count > left_length // 2) and (right_count > right_length // 2):
                return i

        return -1
        
