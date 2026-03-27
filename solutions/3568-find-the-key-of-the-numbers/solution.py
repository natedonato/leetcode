class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        out = ""
        
        for i in range(4):
            out = str(min(num1 % 10, num2 % 10, num3 % 10)) + out
            num1 //= 10
            num2 //= 10
            num3 //= 10

        return int(out)
        
        

            
