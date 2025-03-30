class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_idx = {}
        for i, char in enumerate(s):
            end_idx[char] = i

        n = len(s)
        l = 0
        r = 0
        size = 1
        output = []
        while l < n:
            char = s[l]
            if end_idx[char] > r:
                size += end_idx[char] - r
                r = end_idx[char]
            
            if l == r:
                output.append(size)
                size = 1
                r += 1

            l += 1

        return output
