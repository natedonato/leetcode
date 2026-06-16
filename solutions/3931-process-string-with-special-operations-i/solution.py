class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            if c == "*":
                if res:
                    res.pop()
            elif c == "#":
                res += res
            elif c == "%":
                res.reverse()
            else:
                res.append(c)
        
        return "".join(res)
