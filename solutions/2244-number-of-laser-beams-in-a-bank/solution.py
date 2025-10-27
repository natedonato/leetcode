class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0
        p = 0

        for r in bank:
            curr = r.count('1')

            if curr > 0:
                count += p * curr
                p = curr

        return count
