class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(0, len(num))):
            if int(num[i]) % 2 == 1:
                return num[0:i+1]

        return ""
