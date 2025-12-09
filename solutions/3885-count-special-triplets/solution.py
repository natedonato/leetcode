class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        l = Counter(nums[0:1])
        r = Counter(nums[1:])
        m = 1_000_000_007
        c = 0

        for num in nums[1:-1]:
            r[num] -= 1
            d = num *2
            if d in l and d in r:
                c += l[d] * r[d]
                c %= m
            l[num] += 1

        return c
