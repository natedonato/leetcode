class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        idx = -1

        for i in range(len(s)):
            if s[i] == "6":
                idx = i
                break

        if idx == -1:
            return num

        digit_place = 10 ** (len(s) - idx - 1)
        return num - (digit_place*6) + (digit_place*9)
