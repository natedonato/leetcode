class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

    # I can be placed before V (5) and X (10) to make 4 and 9. 
    # X can be placed before L (50) and C (100) to make 40 and 90. 
    # C can be placed before D (500) and M (1000) to make 400 and 900.
        integer_val = 0

        i = 0
        while i < len(s):
            current_char = s[i]

            if i < len(s) - 1:
                double_char = current_char + s[i+1] 
                if double_char in vals:
                    integer_val += vals[double_char]
                    i += 2
                    continue
            
            integer_val += vals[current_char]
            i += 1

        return integer_val

                    
            

