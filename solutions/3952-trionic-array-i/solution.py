class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        stage = 1

        for i in range(1, len(nums)):
            prev = nums[i-1]
            c = nums[i]

            if prev == c:
                return False
            if prev > c and stage == 1:
                if i == 1:
                    return False
                stage = 2
            elif prev < c and stage == 2:
                stage = 3
            elif prev > c and stage == 3:
                return False

        return stage == 3
