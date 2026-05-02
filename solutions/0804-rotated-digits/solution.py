class Solution:
    def rotatedDigits(self, n: int) -> int:
        changed = ["2", "5", "6", "9"]
        invalid = ["3", "4", "7"]
        count = 0

        for i in range(2, n + 1):
            s = str(i)
            valid = True
            for n in invalid:
                if n in s:
                    valid = False
                    break
            
            if valid == False:
                continue

            valid = False
            for n in changed:
                if n in s:
                    count += 1
                    valid = True
                
                if valid == True:
                    break

        return count
