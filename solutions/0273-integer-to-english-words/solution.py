class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = {
            1: "One",
            2: "Two", 
            3: "Three", 
            4: "Four", 
            5: "Five", 
            6: "Six", 
            7: "Seven", 
            8: "Eight", 
            9: "Nine"
        }
        teens = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve", 
            13: "Thirteen", 
            14: "Fourteen", 
            15: "Fifteen", 
            16: "Sixteen", 
            17: "Seventeen", 
            18: "Eighteen", 
            19: "Nineteen", 
        }

        tens = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }

        hundred = "Hundred"
        thousand = "Thousand"
        million = "Million"
        billion = "Billion"

        out = []

        # billion
        if num >= 1000000000:
            billions = num % 1000000000000 // 1000000000
            billions_str = self.numberToWords(billions) + " Billion"
            if(billions_str != "Zero Billion"):
                out.append(billions_str)

        # million
        if num >= 1000000:
            millions = num % 1000000000 // 1000000
            millions_str = self.numberToWords(millions) + " Million"
            if(millions_str != "Zero Million"):
                out.append(millions_str)

        # thousand
        if num >= 1000:
            thousands = num % 1000000 // 1000
            thousands_str = self.numberToWords(thousands) + " Thousand"
            if(thousands_str != "Zero Thousand"):
                out.append(thousands_str)

        hundreds_digit = num % 1000 // 100
        if(hundreds_digit != 0):
            out.append(ones[hundreds_digit])
            out.append(hundred)

        tens_digit = num % 100 // 10 * 10
        if(tens_digit == 10):
            teens_key = num % 100
            teens_string = teens[teens_key]
            out.append(teens_string)
        elif(tens_digit != 0):
            tens_string = tens[tens_digit]
            out.append(tens_string)

        ones_digit = num % 10
        if(tens_digit != 10 and ones_digit != 0):
            ones_string = ones[ones_digit]
            out.append(ones_string)

        return " ".join(out)


