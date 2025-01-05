class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_counts = [0] * (len(s) + 1)

        for shift in shifts:
           
            if shift[2] == 0:
                shift_counts[shift[0]] -= 1
                shift_counts[shift[1] + 1] += 1
            else:
                shift_counts[shift[0]] += 1
                shift_counts[shift[1] + 1] -= 1


        a = ord("a")
        output = ""

        print(shift_counts)

        prev_count = 0
        for i in range(len(s)):
            diff = shift_counts[i]
            prev_count += diff
            base_char = ord(s[i]) - a

            next_char = base_char + prev_count
            next_char %= 26

            output += chr(a + next_char)

        return output
