class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        total_count = 0

        digit_count = 0
        first_digit = 1
        l1 = low

        while l1 > 0:
            digit_count += 1
            l1 //= 10

        prev_num = 0
        out = []

        while prev_num < high:
            if first_digit + digit_count > 10:
                digit_count += 1
                first_digit = 1

            # make number
            prev_num = 0
            current_digit = first_digit
            for i in range(digit_count):

                prev_num *= 10
                prev_num += current_digit
                current_digit += 1
            
            if prev_num <= high and prev_num >= low:
                out.append(prev_num)

            first_digit += 1

        return out

