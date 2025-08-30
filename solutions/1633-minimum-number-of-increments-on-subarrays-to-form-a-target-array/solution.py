class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        total = 0
        current = 0

        for n in target:
            if n > current:
                total += n - current
            current = n

        return total
