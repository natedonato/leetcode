class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abcs = {
            "a": 0,
            "b": 0,
            "c": 0
        }
        abc_count = 0

        l = 0
        r = 0
        num = 0
        n = len(s)

        while(r < n):
            char = s[r]
            
            if(abcs[char] == 0):
                abc_count += 1
            abcs[char] += 1

            while(abc_count == 3):
                num += len(s) - r

                char = s[l]
                abcs[char] -= 1
                if(abcs[char] == 0):
                    abc_count -= 1
                
                l += 1
            
            r += 1

        return num
