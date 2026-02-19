class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        current_symbol = s[0]
        current_length = 0
        prev_length = 0
        count = 0
        while i < len(s):
            while i < len(s) and s[i] == current_symbol:
                i += 1
                current_length += 1
            count += min(prev_length, current_length)
            prev_length = current_length
            current_length = 0
            if i < len(s):
                current_symbol = s[i]

        return count
