class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [1] * (right + 1)
        primes[1] = 0
        bounded_primes = []
        output = [-1,-1]
        prev = -1

        if(right <= 2):
            return output

        for i in range(2, right + 1):
            if primes[i] == 1:                    
                if left <= i and i <= right:
                    if(prev == -1):
                        prev = i
                    else:
                        diff = i - prev
                        if(output[0] == -1 or output[1] - output[0] > diff):
                            output = [prev, i]
                        prev = i   

                for n in range(i * i, right + 1, i):
                    primes[n] = 0

        return output
