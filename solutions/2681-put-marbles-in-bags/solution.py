class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        difs = []
        l = len(weights)
        for i in range(0, l - 1):
            difs.append(weights[i] + weights[i+1])

        difs.sort()

        final_difference = 0

        l2 = len(difs)
        for i in range(0,k-1):
            final_difference +=  difs[l2 - 1 - i] - difs[i]

        return final_difference

