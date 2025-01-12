class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        open_brackets = []
        unlocked = []

        for i in range(len(s)):
            if locked[i] == "0":
                unlocked.append(i)
            elif s[i] == "(":
                open_brackets.append(i)
            else:
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while open_brackets and unlocked:
            if(unlocked[-1] > open_brackets[-1]):
                unlocked.pop()
                open_brackets.pop()
            else:
                break

        if not open_brackets and len(unlocked) % 2 == 0:
            return True
        
        return False
        
