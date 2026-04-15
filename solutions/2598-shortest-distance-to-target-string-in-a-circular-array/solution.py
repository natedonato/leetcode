class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        for i in range(n):
            left_idx = (startIndex - i) % n
            right_idx = (startIndex + i) % n

            if words[left_idx] == target or words[right_idx] == target:
                return i

        return -1



