class Solution:
    def numSub(self, s: str) -> int:
        l = 0
        r = 0
        one_count = 0
        sub = 0

        while l < len(s):
            
            while r < len(s) and s[r] == "1":
                one_count += 1
                r += 1

            while l < r:
                sub = (sub + one_count) % 1_000_000_007
                if s[l] == "1":
                    one_count -= 1

                l += 1

            l += 1
            r = max(l,r)

        return sub
                
            
