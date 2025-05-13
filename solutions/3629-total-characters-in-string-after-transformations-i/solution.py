class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        counts = [0] * 26
        for c in s:
            idx = ord(c) - ord('a')
            counts[idx] += 1
        
        while t > 0:
            prev = counts[0]
            counts[0] = 0
            for i in range(1,26):
                temp = counts[i]
                counts[i] = prev
                prev = temp
            
            counts[0] += prev
            counts[1] += prev

            t -= 1

        return sum(counts) % (10**9 + 7)
