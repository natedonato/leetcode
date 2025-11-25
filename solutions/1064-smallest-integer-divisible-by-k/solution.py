class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        n = 1
        rem = 1
        seen = set([rem])

        while rem != 0:
            rem = rem * 10 + 1
            rem %= k
            if rem in seen:
                return -1
            else:
                seen.add(rem)
            n += 1
        
        return n
