class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        out = zip(businessLine, code, isActive)
        out = list(out)
        out.sort()
        print(out)
        out = [e[1] for e in out if e[2] == True and self.checkStr(e[1]) and self.checkBus(e[0])]

        return out 
    def checkBus(self, s):
        return s in ["electronics", "grocery", "pharmacy", "restaurant"]

    def checkStr(self, s):
        if not s:
            return False

        for c in s:
            if c != "_" and not (c >= "a" and c <= "z") and not (c >= "A" and c <= "Z") and not (c >= "0" and c <= "9"):
                print(c)
                return False

        return True
