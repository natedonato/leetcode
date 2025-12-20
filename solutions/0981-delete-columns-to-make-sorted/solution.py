class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        s = list(zip(*strs))
        
        count = 0

        for t in s:
            if t != tuple(sorted(t)):
                count += 1 

        return count
