class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits
        out = set()
        for i in range(len(digits)):
            if digits[i] != 0:
                for j in range(len(digits)):
                    if j != i:
                        for k in range(len(digits)):
                            if k != i and k != j and digits[k] % 2 == 0:
                                out.add(digits[i] * 100 + digits[j] * 10 + digits[k])

        return sorted(list(out))

