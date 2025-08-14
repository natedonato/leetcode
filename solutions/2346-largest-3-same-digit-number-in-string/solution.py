class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = -1

        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i]== num[i+2]:
                best = max(best, int(num[i]))

        return "" if best == -1 else str(best) * 3
        
