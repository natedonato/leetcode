class Solution:
    def reinitializePermutation(self, n: int) -> int:
        initial = []
        for i in range(n):
            initial.append(i)

        perm = initial.copy()

        def permutate(perm):
            arr = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    arr[i] = perm[i // 2]
                else: 
                    arr[i] = perm[n // 2 + (i - 1) // 2]
            return arr

        ops = 1
        perm = permutate(perm)

        while(True):
            if perm == initial:
                return ops
            else:
                ops += 1
                perm = permutate(perm)
