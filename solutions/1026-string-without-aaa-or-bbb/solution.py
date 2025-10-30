class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        # equal: just alternate
        # unequal: do two in a row of the one with more
        # 
        #
        #
        #
        #
        out = []
        while a > 0 and b > 0:

            if a > b:
                out.append("aab")
                a -= 2
                b -= 1
            elif b > a:
                out.append("bba")
                b -= 2
                a -= 1
            else:
                if out and out[-1] == "a":
                    out.append("b")
                    out.append("a")
                    a -= 1
                    b -= 1
                else:
                    out.append("a")
                    out.append("b")
                    a -= 1
                    b -= 1
            
        if a > 0:
            out.append("a" * a)
        if b > 0:
            out.append("b" * b)
        
        return "".join(out)
