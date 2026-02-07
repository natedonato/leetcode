class Solution:
    def minimumDeletions(self, s: str) -> int:


        a_count = s.count("a")
        min_delete = a_count
        b_count = 0

        if a_count == 0:
            return 0

        for i in range(len(s)):
            next_char = s[i]
            if next_char == "a":
                a_count -= 1
            elif next_char == "b":
                if b_count != i:
                    min_delete = min(min_delete, a_count + b_count)

                b_count += 1

        if b_count == 0:
            return 0

        return min(min_delete, b_count)
