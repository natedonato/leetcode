class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        best_gain = 0
        one_count = 0

        prev_zero_length = 0
        current_zero_length = 0

        for i, c in enumerate(s):
            if (i == 0 or s[i-1] == "1") and c == "0":
                prev_zero_length = current_zero_length
                current_zero_length = 0

            if c == '0':
                current_zero_length += 1

            if s[i] == "1" and i > 0 and s[i-1] == "0":
                if prev_zero_length != 0:
                    best_gain = max(best_gain, prev_zero_length + current_zero_length)

            if c == '1':
                one_count += 1

        if prev_zero_length != 0:
            best_gain = max(best_gain, prev_zero_length + current_zero_length)

        return best_gain + one_count
            

        
