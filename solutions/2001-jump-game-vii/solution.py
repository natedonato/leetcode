class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != "0":
            return False 

        diff = [0] * len(s)
        curr = 0
        
        for i, c in enumerate(s):
            curr += diff[i]
            if i == 0 or curr > 0 and c == "0":
                if minJump + i < len(s):
                    diff[minJump + i] += 1
                if i+ maxJump + 1 < len(s):
                    diff[i+ maxJump + 1] -= 1
                
        return curr > 0
