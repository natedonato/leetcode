class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ""

        # 1 => A
        # 26 => Z
        # 27 => AA
        columnNumber -= 1
  

        while columnNumber >= 0:
            remainder = (columnNumber) % 26
            char = chr(ord("A") + remainder)
            output = char + output
            columnNumber //= 26
            columnNumber -= 1
        return output
